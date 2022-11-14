
import requests
from http import cookiejar
import fake_useragent


class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

with requests.Session() as session:
    session.cookies.set_policy(BlockAll())
    response = session.get(input("URL: "), headers={
        'user-agent': fake_useragent.UserAgent().random
    })

with open("page.html", "w") as file:
    file.write(response.text)
print(response.text)
