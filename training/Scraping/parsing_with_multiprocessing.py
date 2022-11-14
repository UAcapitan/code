
import multiprocessing
import sys
import requests
from bs4 import BeautifulSoup
import fake_useragent


sys.setrecursionlimit(25000)

SITE_URL = "https://webscraper.io"
URL = "https://webscraper.io/test-sites/e-commerce/allinone-popup-links/computers/laptops"

headers = {
    'user-agent': fake_useragent.UserAgent().random
}

table = []

def handler(elem):
        p_href = elem.find("a", {"class": "title"}).get("onclick").replace("window.open('", "")
        page_href = p_href.split(",")[0][:-1]

        page = requests.get(f"{SITE_URL}{page_href}", headers=headers).text
        page_soup = BeautifulSoup(page, "html.parser")

        page_name = page_soup.find("div", {"class": "caption"}).find_all("h4")[1].text
        
        table.append([
            page_name,
            elem.find("h4", {"class": "price"}).text,
            elem.find("p", {"class": "description"}).text
        ])

        print(table[-1])

def parse():
    laptops = requests.get(URL, headers=headers).text
    soup = BeautifulSoup(laptops, "html.parser")

    elements = soup.find_all("div", {"class": "thumbnail"})

    with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
        process.map(handler, elements)

    return table


if __name__ == "__main__":
    parse()
