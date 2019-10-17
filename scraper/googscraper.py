import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = requests.get(self.site)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.findAll('a'):
            url = tag.get('href')
            if url and 'articles' in url:
                link = 'http://news.google.com' + str(url).replace('.', '', 1)
                all_links.append(link)
                print("\n" + url)

all_links = []
Scraper('http://news.google.com/').scrape()

no_dupes = list(set(all_links))
with open('headlines.txt', 'w') as headlines:
    for link in no_dupes:
        headlines.write("\n" + str(link))