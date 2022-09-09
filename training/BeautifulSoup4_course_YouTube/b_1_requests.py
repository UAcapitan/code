
import requests


responce = requests.get("https://icanhazip.com").text
print(responce)
