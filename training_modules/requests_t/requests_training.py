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

response = requests.get('https://httpbin.org/get')

print(response.status_code, end='\n\n')
print(response.text, end='\n\n')
print(response.json(), end='\n\n')

url = 'https://httpbin.org/post'
query = [('search_car','kia')]

response = requests.post(url, data=query)
response = requests.put(url, data=query)
response = requests.patch(url, data=query)
response = requests.delete(url)
response = requests.head(url)
response = requests.options(url)

