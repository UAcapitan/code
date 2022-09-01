
import json
from urllib.request import urlopen
from urllib.parse import urlencode
import requests
import duckpy


# First example with urllib
def result_urllib():
    params = dict(q='Sausages', format='json')
    handle = urlopen('http://api.duckduckgo.com' + '?' + urlencode(params))
    raw_text = handle.read().decode('utf-8')
    parsed = json.loads(raw_text)

    results = parsed['RelatedTopics']
    for r in results:
        if 'Text' in r:
            print(r['FirstURL'] + ' - ' + r['Text'])

# Second example with requests
def result_requests():
    params = dict(q='Sausages', format='json')
    parsed = requests.get('http://api.duckduckgo.com/', params=params).json()

    results = parsed['RelatedTopics']
    for r in results:
        if 'Text' in r:
            print(r['FirstURL'] + ' - ' + r['Text'])

# Third example with duckpy
def result_duckpy():
    for r in duckpy.Client().search("Sausages"):
        print(r.url + ' - ' + r.description)


if __name__ == "__main__":
    result_urllib()
    print('-'*17)
    result_requests()
    print('-'*17)
    result_duckpy()
