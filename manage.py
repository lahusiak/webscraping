import base
from bs4 import BeautifulSoup
import requests


url = 'https://www.nraila.org/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
news_data = {}
news_list = []
g_data = soup.find_all("div", {"class": "news-item"})
links = soup.find_all('a', {'class': 'news-article-headline'})
resp_list = []

class SoupMakerHandler(base.BaseHandler):
    def get(self):

        for item in g_data:
            headline = (item.contents[1].find_all("div", {"class": "news-article-headline"})[0].text)
            date = (item.contents[1].find_all("p", {"class": "news-date"})[0].text)
            url = (item.contents[1].find_all("div", {"class": "news-article-headline"})[0].a.get('href'))
            resp = {
                'headline': headline,
                'date': date,
                'url': url
            }
            resp_list.append(resp)
        self.api_response(resp_list)





        #     news_list.append(news_object)
        # return news_list
        # do the scraping stuff here!

        # do the selecting organizing of data here!

        # resp = {
        #         'url': 'http://www.google.com',
        #         'title': 'This is google',
        #         'date': '07/14/2016'
        #         }

        # self.api_response(resp)