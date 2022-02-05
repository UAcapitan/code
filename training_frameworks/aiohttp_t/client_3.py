import asyncio
import aiohttp

async def main():
    params = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url='http://httpbin.org/get', params=params) as request:
            print(str(request.url))

if __name__ == '__main__':
    asyncio.run(main())