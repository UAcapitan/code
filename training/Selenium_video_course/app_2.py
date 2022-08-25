from selenium import webdriver

# Settings for FireFox
option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')

browser = webdriver.Firefox(options=option)
browser.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
browser.close()