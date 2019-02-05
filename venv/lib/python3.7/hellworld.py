
"""Script to gather news outlet IP's and return highest ranking of countries mentioned."""
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




def main():
    """Main entry point for the script."""
    pullpage = ip_checker()
    pass

def ip_checker(url):
    """Recurring Store the IP, Geolocation, news outlet name of the website - assign ID to newsoutlet"""
    pass

def Geo_checker(url):
    """Store Geolocation, news outlet name of the website - assign ID to newsoutlet"""
    pass

def country_keywords(url):
    """store country names that are mentioned in XML  - match to ip_checker ID"""
    pass

def most_popular_news():
    """ranks the most mentioned country_keywords by count per day"""
    pass

def visualize_most_popular_news():
    """Visualizes most_popular_news"""
    pass

def stockmarket_week(url,csv):
    """recurring pull topline stock market trends from date to week"""
    pass

def stockbreakdown_country():
    """Breakdown stock performance by country"""
    pass

def stockbreakdown_highinv():
    """Breakdown by highest investment count and sum"""
    pass

def stockbreakdown_buyingprice():
    """List all stock in the coutry by available buying price"""
    pass

def visualize_stockbreakdown():
    """visulaize the stockmarket in a linechart"""
    pass

def time_matching():
    """Use same timeframe for most_popular news breakdown"""
    pass

def split_screen():
    """Split visualize_most_popular_news and visualize_stockbreakdown"""
    pass




