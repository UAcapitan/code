
import json
import requests
from bs4 import BeautifulSoup


def get_js(elem):
    return elem.find("div", {"id": "javascript_check"}).text

def get_cookie(elem):
    return elem.find("div", {"id": "cookie_check"}).text

def get_flash(elem):
    return elem.find("div", {"id": "flash_version"}).text

def main():
    with open("config.json") as file:
        config = json.load(file)

    print(config)

    response = requests.get("https://browser-info.ru/").text
    soup = BeautifulSoup(response, 'html.parser')

    if config['js']: print(get_js(soup))
    if config['cookie']: print(get_cookie(soup))
    if config['flash']: print(get_flash(soup))


if __name__ == "__main__":
    main()
