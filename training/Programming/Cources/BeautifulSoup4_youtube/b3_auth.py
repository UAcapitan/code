
import requests
from bs4 import BeautifulSoup
import fake_useragent
import keys


URL = "https://cloud.webscraper.io/login"

headers = {
    'user-agent': fake_useragent.UserAgent().random
}

# Login with session
with requests.Session() as session:
    form_token = session.get(URL, headers=headers).text
    form_soup = BeautifulSoup(form_token, "html.parser")
    value = form_soup.find("input", {"name": "_token"})["value"]

    data = {
        "_token": value,
        "login": keys.LOGIN,
        "password": keys.PASSWORD
    }

    response = session.post(URL, headers=headers, data=data)
    print(response.status_code)

    # Saving cookies
    cookies = [
        [key.domain, key.name, key.path, key.value]
        for key in session.cookies
    ]

    for cookie in cookies:
        print(cookie)

# New session with previous cookies from old session
with requests.Session() as session2:
    for cookie in cookies:
        session2.cookies.set(domain=cookie[0], name=cookie[1], path=cookie[2], value=cookie[3])

    URL = "https://cloud.webscraper.io/sitemaps"

    response = session2.get(URL, headers=headers)
    print(response.status_code)
