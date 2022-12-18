from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("--proxy-server=184.191.162.4:3128")

browser = webdriver.Chrome(options=option)
browser.get("https://icanhazip.com")