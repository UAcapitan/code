import asyncio
import aiohttp


async def main():
    dict_data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post('http://httpbin.org/post', data=dict_data) as request:
            print(await request.text())


if __name__ == '__main__':
    asyncio.run(main())