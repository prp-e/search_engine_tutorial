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

    content = BeautifulSoup(response.text, 'lxml')
    links = content.findAll('a')

    # Information from the link 
    #   1. URL
    #   2. Title (<title></title>)
    #   3. A lot of words! (<p></p>)

    try:
        title = content.find('title').text 
        description = ''

        for p in content.findAll('p'):
            description += p.text.strip().replace('\n', ' ')
    except:
        return 

    result = {
        'title': title, 
        'url': url, 
        'description': description[64:]
    }

    print(result)