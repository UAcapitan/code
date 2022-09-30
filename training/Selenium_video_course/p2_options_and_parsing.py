from selenium import webdriver
from selenium.webdriver.common.by import By

# Settings for FireFox
option = webdriver.FirefoxOptions()
option.set_preference('general.useragent.override', 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0')
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')

browser = webdriver.Firefox(options=option)
browser.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
browser.quit()

# Settings for Chrome
option = webdriver.ChromeOptions()
option.headless = True

# Parsing nicknames from site
browser = webdriver.Chrome(options=option)
browser.get("https://nick-name.ru/generate/")

list_ = []

for _ in range(10):
    xpath = '/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
    browser.find_element(By.XPATH, xpath).click()

    xpath = "/html/body/div/div[1]/div[1]/div[2]/form/table/tbody/tr[6]/td[2]/input"
    list_.append(browser.find_element(By.XPATH, xpath).get_attribute("value"))

for link in list_:
    print(link)

browser.quit()