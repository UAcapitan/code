
import requests_html
import fake_useragent
from http import cookiejar


URL = input("URL: ")

headers = {
    'user-agent': fake_useragent.UserAgent().random
}

class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

with requests_html.HTMLSession() as session:
    session.cookies.set_policy(BlockAll())
    response = session.get(URL, headers=headers)

if input("Save file (y or n)?: ") == "y":
    with open("page.html", "w") as file:
        file.write(response.text)
