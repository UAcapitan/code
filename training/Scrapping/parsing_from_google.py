'''
    How to install geckodriver (Firefox driver):

    pip install webdrivermanager
    webdrivermanager firefox --linkpath <path>
'''

import json
import requests
from bs4 import BeautifulSoup
from fp.fp import FreeProxy


class GoogleSearch:
    def __init__(self, query: str, headers: dict):
        URL = self.get_url(query)

        self.headers = headers

        self.page = self.get_page(URL, self.headers)

        self.json = {
            "query": query,
            "url": URL,
            "status": self.page.status_code,
        }

    def get_url(self, query: str) -> str:
        return f"https://www.google.com/search?q={query}"

    def get_page(self, url: str, headers: dict):
        PROXY = FreeProxy(country_id=['US'], timeout=1, rand=True).get()

        with requests.Session() as session:
            self.response = session.get(url, headers=headers, proxies={"http": PROXY})

        return self.response

    def parse(self, pages: int):
        self.json["pages"] = []

        for _ in range(pages):
            after_process = []

            soup = BeautifulSoup(self.page.text.strip(), "html.parser")

            articles = soup.find("div", {"id": "search"}).find("div").find("div")

            for article in articles:
                try:
                    article_data = {}
                    name = article.find("h3").text.strip()

                    if name in [
                        'Відео',
                        'Зображення'
                    ]:
                        # after_process.append(article)
                        continue
                    elif name == "Головні новини":
                        print(self.extra_parse(article))

                    article_data["name"] = name
                    article_data["url"] = article.find("a").get("href")
                    article_data["description"] = article.find_all("span")[-1].text.strip()
                    
                    self.json["pages"].append(article_data)
                except:
                    print("Error")
                    continue

            next_page = soup.find("table", {"role": "presentation"}).find_all("td")[-1].find("a").get("href")
            self.page = self.get_page(f"https://www.google.com{next_page}", self.headers)

    def extra_parse(self):
        pass

if __name__ == "__main__":
    headers={
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
    }

    google = GoogleSearch("Python", headers)
    google.parse(3)
    # print(json.dumps(google.json, sort_keys=False, indent=4))
