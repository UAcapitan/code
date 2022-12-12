
import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run(users):
    options = webdriver.ChromeOptions()

    with webdriver.Chrome(options=options) as driver:
        for user in users:
            driver.get("http://127.0.0.1:5000/login")

            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "email")))
            except:
                continue

            driver.find_element(by=By.NAME, value="email").send_keys(user["email"])
            driver.find_element(by=By.NAME, value="password").send_keys(user["password"])

            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "reg__submit")))

            driver.find_element(by=By.CLASS_NAME, value="reg__submit").click()

            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "main_content__link")))
            except:
                continue

            href = driver.find_element(by=By.CLASS_NAME, value="main_content__link").get_attribute("href")

            for _ in range(1, random.randint(3,17)):
                number = random.randint(1, int(href.split("/")[-1]))
                driver.get(f"http://127.0.0.1:5000/question/{str(number)}/like")

            for _ in range(1, random.randint(3,17)):
                number = random.randint(1,91)
                driver.get(f"http://127.0.0.1:5000/profile/{str(number)}/follow")
            
            driver.get(f"http://127.0.0.1:5000/logout")


if __name__ == "__main__":
    with open("users_data.csv", "r") as file:
        reader = csv.reader(file)
        users = []
        for user in reader:
            users.append({
                "email": user[0],
                "password": user[1]
            })

    run(users)
