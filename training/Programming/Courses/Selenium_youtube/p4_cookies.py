
import time
import pickle
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.work.ua/")
time.sleep(100)

pickle.dump(browser.get_cookies(), open("session", "wb"))

cookies = pickle.load(open("session", "rb"))
print(cookies)

browser.quit()
