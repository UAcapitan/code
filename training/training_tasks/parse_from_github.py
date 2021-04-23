import requests
from bs4 import BeautifulSoup
import json
import datetime

url = 'https://github.com/UAcapitan?tab=overview&from=2021-04-01&to=2021-04-23'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('rect', class_='ContributionCalendar-day')

list_commits = []

for quote in quotes:
    try:
        list_commits.append(int(quote["data-count"]))
    except:
        continue

today = datetime.datetime.now()
today_number = int(today.strftime('%j'))

list_commits = list_commits[int(input()):today_number]


with open('list_commits.json', 'w') as file:
    json.dump({'list_commits':list_commits}, file)