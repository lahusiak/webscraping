#from this tutorial: https://www.youtube.com/watch?v=3xQTJi2tqgk

import requests
from bs4 import BeautifulSoup

url = ''
r = requests.get(url)

soup = BeautifulSoup(r.content)

#Example
links = soup.find_all('a')

for link in links:
    print "<a href='%s'>%s</>" %(link.get("href"), link.text)

#Div content
g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
    #list of items
    print item
    #first item in list above
    print item.contents[0].text
    print item.contents[1].find_all("a", {"class": "business-name"})
    print item.contents[1].find_all("p", {"class": "adr"})[0].text
    print item.contents[1].find_all("span", {"itemprop": "address"})[0].text
    print item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text
    try:
    print item.contents[1].find_all("p", {"class": "primary"})[0].text
except:
    pass
