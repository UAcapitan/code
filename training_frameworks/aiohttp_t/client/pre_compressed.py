import asyncio
import aiohttp
import zlib


async def compressed(my_data):
    return zlib.compress(my_data)

async def main():
    data = b'Text'
    headers = {'Content-Encoding': 'deflate'}
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url='http://httpbin.org/post',
            data=await compressed(data),
            headers=headers
        ) as request:
            print(await request.text())


if __name__ == '__main__':
    asyncio.run(main())