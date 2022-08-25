from selenium import webdriver
from selenium.webdriver.common.by import By

# Settings for FireFox
option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')

browser = webdriver.Firefox(options=option)
browser.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
browser.quit()

browser = webdriver.Chrome()
browser.get("https://nick-name.ru/generate/")

list_ = []

for _ in range(10):
    xpath = '/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
    browser.find_element(By.XPATH, xpath).click()

browser.quit()