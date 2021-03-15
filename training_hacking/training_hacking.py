import requests

list_sites = [
    'https://www.google.com/',
    'https://www.youtube.com/',
    'https://github.com/',
    'https://www.codewars.com',
    'https://habr.com/ru/top/'
]

def go_in_site(n, index_site):
    if n < 100:
        n = 100
    for i in range(n):
        try:
            print('{} - {}'.format(list_sites[index_site], requests.get(list_sites[index_site])))
        except:
            print('Error')

for index_site in range(len(list_sites)):
    go_in_site(int(input()), index_site)