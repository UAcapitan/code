
import time
import requests
from bs4 import BeautifulSoup
import fake_useragent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


SITE_URL = "https://webscraper.io"
URL = "https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops"

headers = {
    'user-agent': fake_useragent.UserAgent().random
}

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get(URL)

page = driver.find_element(By.TAG_NAME, "html")

for _ in range(10):
    time.sleep(3)
    for _ in range(7):
        page.send_keys(Keys.DOWN)

response = driver.page_source
soup = BeautifulSoup(response, "html.parser")

laptops = soup.find_all("div", {"class": "thumbnail"})

table = []

for laptop in laptops:
    page_href = laptop.find("a", {"class": "title"}).get("href")

    page = requests.get(f"{SITE_URL}{page_href}", headers=headers).text
    page_soup = BeautifulSoup(page, "html.parser")

    try:
        page_name = page_soup.find("div", {"class": "caption"}).find_all("h4")[1].text
    
        table.append([
            page_name,
            laptop.find("h4", {"class": "price"}).text,
            laptop.find("p", {"class": "description"}).text
        ])
    except IndexError:
        pass

for t_elem in table:
    print(t_elem)
