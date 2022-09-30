
import requests
import fake_useragent
from bs4 import BeautifulSoup


page = requests.get("https://browser-info.ru", headers={
    'user-agent': fake_useragent.UserAgent().random
}).text

soup = BeautifulSoup(page, "html.parser")

INFO = "No information"

elements = [
    soup.find("div", {"id": "javascript_check"}).text,
    soup.find("div", {"id": "cookie_check"}).text,
    soup.find("div", {"id": "flash_version"}).text,
    soup.find("div", {"id": "browser_lang"}).text or INFO,
    soup.find("div", {"id": "window_size"}).text or INFO,
    soup.find("div", {"id": "user_agent"}).text.strip() or INFO,
    soup.find("div", {"id": "plugins_total"}).text or INFO,
]

for i in elements:
    print(i)
