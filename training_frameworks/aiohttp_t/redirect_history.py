import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:5000') as request:
            for i in request.history:
                print(i.url)
            print(request.url)

if __name__ == '__main__':
    asyncio.run(main())