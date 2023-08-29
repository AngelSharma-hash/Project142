import numpy as np 
import pandas as pd

data = pd.read_csv('articles.csv')

output = []
data = data.sort_values('movies')
def Sort_Values():
    
    output = data['movies','url','contentType','lang','contentId','authorPersonId','title'].head(20).values.tolist()