import asyncio
import aiohttp

async def main():
    URL = 'http://127.0.0.1:8000/api/v1/auth/token/login'
    json_data = {
        'username':'admin',
        'password':'root'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url=URL, json=json_data) as request:
            print(await request.json())

if __name__ == '__main__':
    asyncio.run(main())