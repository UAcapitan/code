import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'ZmViNDE5MzQtNDEyZS00NGY2LTlhY2QtZTdkNTY4MmYyY2MxOmExMmY2MGZmN2FiMjRlODRiZTRhYTIxN2RmMjI0NjZl'

headers_auth = {'Authorization':'Basic '+KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    TOKEN = auth.text
    
    while True:
        word = input('Input word for translate or "q" for exit: ')
        if word == 'q':
            exit()
        headers_translate = {
            'Authorization':'Bearer ' + TOKEN
        }
        params_translate = {
            'text':word,
            'srcLang':1033,
            'dstLang':1049
        }
        result = requests.get(URL_TRANSLATE, headers=headers_translate, params=params_translate)
        res = result.json()
        try:
            print(res['Translation']['Translation'])
        except:
            print('Не найдено разультатов')

else:
    print('Error')
    exit()