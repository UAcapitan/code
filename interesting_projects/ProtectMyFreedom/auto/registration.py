
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import generator_of_users

def run(users):
    options = webdriver.ChromeOptions()

    with webdriver.Chrome(options=options) as driver:
        for user in users:
            driver.get("http://127.0.0.1:5000/reg")

            driver.find_element(by=By.NAME, value="username").send_keys(user["username"])
            driver.find_element(by=By.NAME, value="email").send_keys(user["email"])
            driver.find_element(by=By.NAME, value="password").send_keys(user["password"])
            driver.find_element(by=By.NAME, value="re_password").send_keys(user["password"])

            time.sleep(1)

            driver.find_element(by=By.CLASS_NAME, value="reg__submit").click()

            time.sleep(1)

            try:
                driver.find_elements(by=By.CLASS_NAME, value="nav-link")[-1].click()

                time.sleep(3)
            except:
                continue


if __name__ == "__main__":
    users = [
        generator_of_users.generated_data() for _ in range(700)
    ]

    run(users)
