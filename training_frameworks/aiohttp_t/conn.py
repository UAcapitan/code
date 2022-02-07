import asyncio
import aiohttp

async def main():
    conn = aiohttp.TCPConnector(limit=50, limit_per_host=5)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get('http://httpbin.org/get') as request:
            print(await request.text())

if __name__ == '__main__':
    asyncio.run(main())