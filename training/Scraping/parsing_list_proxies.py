
import requests
from bs4 import BeautifulSoup
import fake_useragent
import json


URL = "https://free-proxy-list.net/"

headers = {
    'user-agent': fake_useragent.UserAgent().random
}

def save_json(file_json: list) -> None:
    with open("proxies.json", "w") as file:
        json.dump({
            "proxies": file_json
        }, file)

def parse() -> list:
    page = requests.get(URL, headers=headers).text
    soup = BeautifulSoup(page, "html.parser")

    table_soup = soup.find("table")
    all_tr = table_soup.find_all("tr")[1:]

    table = []

    for elem in all_tr:
        ip, port = elem.find_all("td")[:2]
        table.append(
            f"{ip.text}:{port.text}"
        )

    save_json(table)

    return table


if __name__ == "__main__":
    for proxy in parse():
        print(proxy)
