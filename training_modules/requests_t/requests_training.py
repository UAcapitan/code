import requests

response = requests.get('https://google.com')
print(response.status_code)

if response.status_code == 200:
    print('Success')
    print(response.text, end='\n\n')
    print(response.headers, end='\n\n')
    print(response.headers['Content-Type'], end='\n\n')
else:
    print('Error')

response = requests.get('https://google.com/search', params=[('q','Hi')])

print(response.status_code, end='\n\n')
print(response.url, end='\n\n')

response = requests.post('https://httpbin.org/post', data=[('key','value')])

print(response.status_code, end='\n\n')
print(response.url, end='\n\n')
print(response.request.body, end='\n\n')