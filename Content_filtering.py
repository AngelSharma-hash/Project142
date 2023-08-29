from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

data = pd.read_csv('articles.csv')
data = data[data['title'].notna()]
data = data[data['soup'].notna()]

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(data['soup'])
count_matrix = count.fit_transform(data['title'])

data = data.reset_index()
indices = pd.Series(data.index, index=data['contentId'])

def get_recommendations(title, cosine_sim):
   idx = indices[title]
   sim_scores = list(enumerate(cosine_sim[idx]))
   sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
   sim_scores = sim_scores[1:11]
   article_indices = [i[0] for i in sim_scores]
   return data['title'].iloc[article_indices]

