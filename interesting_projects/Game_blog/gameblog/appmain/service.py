from django.shortcuts import render
import aiohttp

def error(request, text):
    return render(request, 'appmain/error_page.html', {'error': text})

async def get_token():
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url='http://localhost:8000/api/v1/auth/token/login',
                json = {
                    'Password': 'rootrootroot',
                    'Username': 'admin'
                }
            ) as response:
                result = await response.json()
        return result