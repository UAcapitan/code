
import requests
from multiprocessing.pool import ThreadPool


def handler(query: str):
    with requests.Session() as session:
        url = f"https://www.google.com/search?q={query}"
        response = session.get(url)
        print(response.status_code)
        

if __name__ == "__main__":
    p = ThreadPool(7)
    p.map(handler, [str(i) for i in range(100)])
