import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
URL_WORDFORMS = 'https://developers.lingvolive.com/api/v1/WordForms'
KEY = 'ZmViNDE5MzQtNDEyZS00NGY2LTlhY2QtZTdkNTY4MmYyY2MxOmExMmY2MGZmN2FiMjRlODRiZTRhYTIxN2RmMjI0NjZl'

point = 0

headers_auth = {'Authorization':'Basic '+KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    TOKEN = auth.text

    point = int(input('Choose\n1.Translate\n2.Wordforms\n'))
    
    while True:
        word = input('Input word for translate or "q" for exit: ')
        if word == 'q':
            exit()

        headers_translate = {
            'Authorization':'Bearer ' + TOKEN
        }

        if point == 1:
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
                print('Results not founded')

        if point == 2:
            params_translate = {
                'text':word,
                'lang':1033
            }
            result = requests.get(URL_WORDFORMS, headers=headers_translate, params=params_translate)
            res = result.json()
            try:
                print('\
Past - {}\n\
Present - {}\n\
Continuous - {}'
                .format(
                    res[1]['ParadigmJson']['Groups'][0]['Table'][0][1]['Value'],
                    res[1]['ParadigmJson']['Groups'][0]['Table'][1][1]['Value'],
                    res[1]['ParadigmJson']['Groups'][0]['Table'][2][1]['Value'],
                    )
                )
            except:
                print('Не найдено разультатов')


else:
    print('Error')
    exit()