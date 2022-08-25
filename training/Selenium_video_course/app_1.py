from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# Clicks
browser.get("https://youtube.com")
browser.find_element(By.XPATH, '//*[@id="content"]').click()

browser.get("https://youtube.com")
browser.find_element(By.XPATH, '//*[@id="content"]').click()

# Get attributes
browser.get("https://youtube.com")
videos = browser.find_elements(By.XPATH, '//*[@id="content"]')

for video in videos:
    print(video.get_attribute("class"))

# Input data in form
xpath = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer'
browser.find_element(By.XPATH, xpath).click()
xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form\
/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
browser.find_element(By.XPATH, xpath).send_keys('test@gmail.com')

# Scrolling
browser.get("https://youtube.com")
html = browser.find_element(By.TAG_NAME, "html")

for i in range(100):
    html.send_keys(Keys.DOWN)
