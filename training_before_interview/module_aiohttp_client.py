import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as res:
            print(res.status)

if __name__ == "__main__":
    asyncio.run(main())