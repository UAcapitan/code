from email import header
import json
from typing import ParamSpecArgs
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"}
page = requests.get('https://www.gallaudet.edu/tutorial-and-instructional-programs/english-center/grammar-and-vocabulary/verbs/irregular-verb-list/', headers=headers).text.strip()
# print(page)

soup = BeautifulSoup(page, "html.parser")
result = soup.find_all("table")

verbs = {}

for i in result:
    for j in i.find_all('tr'):
        k = j.find_all('td')
        try:
            verbs[k[0].text] = [k[0].text, k[1].text, k[2].text]
        except:
            pass

# print(verbs)

# with open('verbs.json', 'w') as file:
#     json.dump(verbs, fp=file)