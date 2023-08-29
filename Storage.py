import csv
import pandas as pd
import numpy as np

All_books = []

with open('articles.csv', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    csv.field_size_limit(100000000)
    data2 = list(reader)
    
    All_books = data2[1:]

liked_articles = []
not_liked_articles = []