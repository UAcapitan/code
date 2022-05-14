import asyncio
import aiohttp


async def main():
    headers = {'Authorization': 'Basic uf39808r39u3ruj=='}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post('http://httpbin.org/post') as request:
            json_body = await request.json()
            print(json_body)
            print(json_body['headers']['Authorization'])


if __name__ == '__main__':
    asyncio.run(main())