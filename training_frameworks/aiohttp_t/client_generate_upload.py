import asyncio
import aiohttp
import aiofiles


async def filesender():
    async with aiofiles.open('client.py', 'rb') as f:
        chunk = await f.read(10)
        while chunk:
            yield chunk
            chunk = await f.read(10)

async def main():
    
    async with aiohttp.ClientSession() as session:
        async with session.post('http://httpbin.org/post', data=filesender()) as request:
            print(await request.text())


if __name__ == '__main__':
    asyncio.run(main())