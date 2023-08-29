from flask import Flask, jsonify,request
import csv
import pandas as pd
from Storage import liked_articles
from Storage import not_liked_articles, All_books
from DemographicFiltering import output
from Content_filtering import get_recommendations

app = Flask(__name__)

data = pd.read_csv('articles.csv')
data.rename(columns = {'': 'id'},inplace=True)


@app.route('/get_articles')
def get_articles():
    return jsonify({'data':All_books[0], 'status':'success'})

@app.route('/like_the_article', methods=['POST'])
def movies_liked():
    global All_books
    global liked_articles
    articles = All_books[0]
    All_books = All_books[1:]
    liked_articles.append(articles)
    return jsonify({'status':'success'}), 201

@app.route('/not_like_the_article', methods=['POST'])
def movies_not_liked():
    global All_books
    global not_liked_articles
    articles = All_books[0]
    All_books = All_books[1:]
    not_liked_articles.append(articles)
    return jsonify({'status':'success'}), 201

@app.route('/popular_books')
def popular_books():
    article_data=[]
    for books in output:
        data ={
            'title':books[-1],
            'total_events':books[0],
            'url':books[1],
            'language':books[3],
            'contentType':books[2],
            'contentId':books[4],
            'authorPersonId':books[5]
        }
        article_data.append(data)
    return jsonify({'data':article_data, 'status':'success'}),200

@app.route('/recommendations')
def get_recommendations():
    recommended_articles = []
    for i in liked_articles:
        output = get_recommendations(i[19])
        for data in output:
            recommended_articles.append(data)
        import itertools 
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended, _ in itertools.groupby(all_recommended))
    
    article_data = []

    for recommended in recommended_articles:
        data = {
            'title':recommended[-1],
            'total_events':recommended[0],
            'url':recommended[1],
            'language':recommended[3],
            'contentType':recommended[2],
            'contentId':recommended[4],
            'authorPersonId':recommended[5]
        }
        article_data.append(data)
    return jsonify({'data':article_data, 'status':'success'}),200


if __name__=='__main__':
    app.run()
