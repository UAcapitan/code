
import grequests


urls = [
    "https://google.com",
    "https://youtube.com",
    "https://news.google.com/",
]

rs = (grequests.get(url) for url in urls)

if __name__ == "__main__":
    results = grequests.map(rs)

    print(results)
