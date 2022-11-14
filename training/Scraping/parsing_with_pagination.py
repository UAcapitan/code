
import requests
from bs4 import BeautifulSoup
import fake_useragent


SITE_URL = "https://webscraper.io"
URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

headers = {
    'user-agent': fake_useragent.UserAgent().random
}

def parse(count_pages: int = 1) -> list:
    print("Parsing in proccess", end="\n\n")

    info = []

    for page_number in range(1, count_pages + 1):
        response = requests.get(f"{URL}?page={page_number}")
        soup = BeautifulSoup(response.text, "html.parser")
        blocks = soup.find_all("div", {"class": "thumbnail"})

        for block in blocks:
            price = block.find("h4", {"class": "price"}).text

            if float(price[1:]) >= 700:
                page_href = SITE_URL + block.find("a", {"class": "title"}).get("href")
                page_response = requests.get(page_href, headers=headers).text
                page_soup = BeautifulSoup(page_response, "html.parser")
                elem_name = page_soup.find("div", {"class", "caption"}).find_all("h4")[1].text
                list_hdd = page_soup.find_all("button", {"class": "swatch", "disabled": None})
                page_hdd = [elem.text for elem in list_hdd]

                info.append([
                    elem_name,
                    price,
                    block.find("div", {"class": "ratings"}).find_all("p")[1]
                    .get("data-rating") + " score",
                    block.find("div", {"class": "ratings"}).find_all("p")[0].text,
                    block.find("p", {"class": "description"}).text,
                    page_hdd,
                    page_href
                ])

                for item in info[-1]:
                    print(item)
                print()

    print("Parsing is done")
    return info

if __name__ == "__main__":
    parse(7)
