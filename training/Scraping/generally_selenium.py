
from selenium import webdriver


URL = input("URL: ")
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.headless = False

with webdriver.Chrome(options=options) as driver: 
    driver.get(URL)
    response = driver.page_source

if input("Save file (y or n)?: ") == "y":
    with open("page.html", "w") as file:
        file.write(response)
