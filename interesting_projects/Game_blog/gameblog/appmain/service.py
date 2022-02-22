from django.shortcuts import render
import requests

def error(request, text):
    return render(request, 'appmain/error_page.html', {'error': text})

def get_api_token(request, username, password):
    try:
        with requests.post(
            url='http://localhost:8000/api/v1/auth/token/login',
            data = {
                'username': username,
                'password': password
            }
        ) as response:
            return response.json()['auth_token']
    except:
        error(request, 'Error')