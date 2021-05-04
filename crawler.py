# Steps for perfoming a web search 
#   1. Crawl the web
#   2. Index the material we just crawled. 
#   3. Performing the search. 
#
# Crawler
#   1. Opens a link 
#   2. Searches for other links in the page
#   3. Does the same for other links. 

from bs4 import BeautifulSoup 
import requests

def crawl(url):
    try:
        print(f'Crawling {url}')
        response = requests.get(url)
    except:
        pass 

    content = BeautifulSoup(url, 'lxml')
    links = content.findAll('a')

    print(len(links))