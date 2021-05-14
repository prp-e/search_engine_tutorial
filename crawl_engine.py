from bs4 import BeautifulSoup 
import crawler
import requests

def engine(url):

    try:
        res = requests.get(url)
    except: 
        return 

    content = BeautifulSoup(res.text, 'lxml')
    links = content.findAll('a')

    external_links = []
    for link in links:
        try:
            if 'http' in link['href']:
                external_links.append(link['href'])
        except KeyError as e:
            pass

    for external_link in external_links: 
        crawler.crawl(external_link, 5)
