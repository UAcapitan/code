
from autoscraper import AutoScraper

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
wanted = ["Asus VivoBook X4...", "$295.99", "14 reviews"]

scrapper = AutoScraper()
result = scrapper.build(url, wanted)

print(result)
