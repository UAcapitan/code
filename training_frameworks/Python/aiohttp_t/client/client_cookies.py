import asyncio
import aiohttp


async def main():
    cookies = {'key':'value'}
    async with aiohttp.ClientSession(cookies=cookies) as session:
        async with session.get('http://httpbin.org/cookies') as request:
            json_body = await request.json()
            print(json_body['cookies'])


if __name__ == '__main__':
    asyncio.run(main())