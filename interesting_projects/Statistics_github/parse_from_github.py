import requests
from bs4 import BeautifulSoup
import json
import datetime

url = f'https://github.com/{input("Name GitHub Account: ")}?tab=overview&from={input("Year: ")}-01-01'
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

print(f'Current day number: {today_number}')
list_commits = list_commits[int(input("From date: ")):int(input("Ending with date: "))]


with open('list_commits.json', 'w') as file:
    json.dump({'list_commits':list_commits}, file)