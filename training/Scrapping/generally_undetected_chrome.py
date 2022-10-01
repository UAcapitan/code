
import undetected_chromedriver as uc


URL = input("URL: ")

with uc.Chrome() as driver:
    driver.get(URL)
    response = driver.page_source

if input("Save file (y or n)?: ") == "y":
    with open("page.html", "w") as file:
        file.write(response)
