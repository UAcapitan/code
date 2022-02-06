import asyncio
import aiohttp


async def main():
    file_data = {
        'file': open('client.py', 'rb')
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post('http://httpbin.org/post', data=file_data) as request:
            print(await request.text())


if __name__ == '__main__':
    asyncio.run(main())