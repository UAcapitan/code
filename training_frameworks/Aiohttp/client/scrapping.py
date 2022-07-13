import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def get_page(session, url):
    async with session.get(url) as r:
        return await r.text()

async def get_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_page(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

async def main(urls):
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, urls)
        return data

def parse(results):
    for html in results:
        soup = BeautifulSoup(html)
        print(soup.find('form', {'class': 'form-horizontal'}).text.strip())
    return "Done"

def parse_books(results):
    list_ = []
    for html in results:
        soup = BeautifulSoup(html)
        names = soup.find_all('article', {'class': 'product_pod'})
        for div in names:
            list_.append([div.find('h3').text.strip(), div.find('p', {'class': 'price_color'}).text.strip()])
    return list_

def print_names(names):
    for name in names:
        print(f"{name[0]} - {name[1]}")


if __name__ == "__main__":
    urls = [
        'https://books.toscrape.com/catalogue/page-1.html',
        'https://books.toscrape.com/catalogue/page-2.html',
        'https://books.toscrape.com/catalogue/page-3.html',
    ]

    results = asyncio.run(main(urls))
    print(len(results))
    print(parse(results))
    print_names(parse_books(results))