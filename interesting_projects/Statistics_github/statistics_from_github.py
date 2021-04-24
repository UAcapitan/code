import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import matplotlib.pyplot as plt

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

rating = 0
rating_list = []

for i in list_commits:
    if i > 0 and i <= 3:
        j = 0
    elif i > 3:
        j = 1
    elif i <= 0:
        j = -2
    rating = rating + j
    if rating < 0:
        rating = 0
    rating_list.append(rating)

list_count = []
j = 1
for i in rating_list:
    list_count.append(j)
    j += 1

data = {'Day': list_count,
        'Unemployment_Rate': rating_list
       }

df = pd.DataFrame(data,columns=['Day','Unemployment_Rate'])
df.plot(x='Day', y='Unemployment_Rate', kind='line')
plt.show()