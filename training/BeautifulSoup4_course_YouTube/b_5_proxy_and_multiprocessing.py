
import requests
import json
import multiprocessing


URL = 'http://icanhazip.com/'

def handler(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

    try:
        requests.get(URL, proxies=proxies, timeout=2)
        print(f"IP: {proxy}")
    except:
        print("Proxy is not valid")


if __name__ == "__main__":
    with open("proxies.json", "r") as file:
        proxies_list = json.load(file)["proxies"]

    with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
        process.map(handler, proxies_list)
