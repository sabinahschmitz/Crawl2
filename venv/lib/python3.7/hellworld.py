

"""Script to gather news outlet IP's and return highest ranking of countries mentioned.Final Test"""
from bs4 import BeautifulSoup
import requests
#Counter helps count the amount of times something was mentioned
from collections import Counter
import csv
import numpy as np

#create the soup
url = 'https://sabinaschmitz.com/test-page/'
page = requests.get(url)

#create soup for HTML pulling
soup = BeautifulSoup(page.content, 'html.parser')

#putting the soup output into country_list
country_list = [content.text for content in soup.select("[class^='sqs-block-content'] p")]

#count the country name mentions in country list
country_count = Counter(country_list)
for key, value in country_count.items():
   print(key, value)



country_keys = np.array(country_count.keys(), dtype=('U25'))
count_vals = np.array(country_count.values(), dtype=str)
website = str(url)

#create csv file countries-per-blog
f = csv.writer(open('countries-per-blog2.csv', 'w'))
#heading of top row
f.writerow(['Country', 'Count', 'Website'])


f.writerow([country_keys, count_vals, website])



#path = 'path/to/a/csvfile'
#r is used for only reading(opening) the file
#read_csv = open(path,'r')
#r+ is used for reading and writing(opening)to the same file
#readwrite_csv = open(path, 'r+')

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




