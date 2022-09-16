
import time
import requests
import cfscrape


def get_session():
    session = requests.Session()
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

URL = "https://www.priceline.com/relax/at/160881803/from/20220913/to/20220914/rooms/1/adults/1"

with get_session() as session:
    for i in range(1,8):
        print(session.get(
            f"https://www.priceline.com/relax/at/160881803/from/20220913/to/20220914/rooms/1/adults/{str(i)}"
        ).status_code)
        time.sleep(2)
