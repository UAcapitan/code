
import requests
import fake_useragent
from bs4 import BeautifulSoup


URL = "https://zastavok.net/"

headers = {
    'user-agent': fake_useragent.UserAgent().random
}

def download_image(src: str) -> None:
    image_content = requests.get(f"{URL}{src[1:]}", headers=headers).content

    name = src.split("/")[-1]
    with open(f"images/{name}", "wb") as file:
        file.write(image_content)

def parser(category: str, page_amount: int = 1) -> str:
    for num_page in range(page_amount + 1):
        page = requests.get(f"{URL}{str(num_page)}", headers=headers).text
        soup = BeautifulSoup(page, "html.parser")
        photo_blocks = soup.find_all("div", {"class": "short"})
        for pb in photo_blocks:
            pb_category = pb.find("span", {"class": "short_wallcat"}).text
            if category == pb_category:
                image_url = pb.find("div", {"class": "short_prev"}).find("a").get("href")
                image_page = requests.get(f"{URL}{image_url[1:]}", headers=headers).text
                image_soup = BeautifulSoup(image_page, "html.parser")
                image_src = image_soup.find("img", {"id": "target"}).get("src")
                download_image(image_src)

    return 'Images were downloaded'


if __name__ == "__main__":
    print(parser("Животные", 7))
