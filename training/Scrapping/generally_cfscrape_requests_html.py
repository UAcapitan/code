
import requests_html
import cfscrape
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

def get_session():
    session = requests_html.HTMLSession()
    session.headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0)   Gecko/20100101 Firefox/69.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'ru,en-US;q=0.5',
        'Accept-Encoding':'gzip, deflate, br',
        'DNT':'1',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1',
        'Pragma':'no-cache',
        'Cache-Control':'no-cache'}
    return cfscrape.create_scraper(sess=session)

with get_session() as session:
    session.cookies.set_policy(BlockAll())
    response = session.get(URL)

    print(response.status_code)

if input("Save file (y or n)?: ") == "y":
    with open("page.html", "w") as file:
        file.write(response.text)