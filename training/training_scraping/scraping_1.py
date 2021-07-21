import urllib.request as urllib2
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/all/'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
price_box = soup.find('a', attrs={'class':'tm-article-snippet__title-link'})
price = price_box.text
print(price)