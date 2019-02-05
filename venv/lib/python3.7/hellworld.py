
"""Script to gather news outlets that return most mentioned countries."""


from bs4 import BeautifulSoup
import requests
#Counter helps count the amount of times something was mentioned
from collections import Counter
import csv
import numpy as np
import pandas as pd

#create the soup
url = 'https://sabinaschmitz.com/test-page/'
page = requests.get(url)

#create soup for HTML pulling
soup = BeautifulSoup(page.content, 'html.parser')

#putting the soup output into country_list
country_list = [content.text for content in soup.select("[class^='sqs-block-content'] p")]

#Counter counts the amounts of mentiones in the dictionary
country_count = Counter(country_list)
#creates a dataframe out of the counted objects
df = pd.DataFrame.from_dict(country_count, orient='index').reset_index()
#renames the colums of the dataframe
df = df.rename(columns={'index':'country name', 0:'count'})


#this exports the dataframe to a csv file
export_csv = df.to_csv(r'/Users/sabinaschmitz/PycharmProjects/Helloworld/dataframe.csv', index=False)
print(df)


