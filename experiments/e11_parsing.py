
import requests
from bs4 import BeautifulSoup

def parser(url: str) -> list:
    html: str = requests.get(url).text
    
    soup: BeautifulSoup = BeautifulSoup(html, "html.parser")

    elements: list = soup.find_all("div", {"class": "thumbnail"})

    items: list = []

    for element in elements:
        item: list = []

        rate: list = element.find("div", {"class": "ratings"}).find_all("p")

        item.extend([
            element.find("a", {"class": "title"}).text.replace("...", ""),
            element.find("div", {"class": "caption"}).find("h4").text,
            element.find("p", {"class": "description"}).text,
            f"{rate[1]['data-rating']}/5",
            rate[0].text
        ])

        items.append(item)
    
    return items

if __name__ == "__main__":
    result: list = parser("https://webscraper.io/test-sites/e-commerce/allinone")

    for item_from_result in result:
        print(item_from_result)
