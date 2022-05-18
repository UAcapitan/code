import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://google.com') as resp:
            print(resp.status)

if __name__ == "__main__":
    asyncio.run(main())