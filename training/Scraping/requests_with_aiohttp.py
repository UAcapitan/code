
import asyncio
import aiohttp

URL = input("URL: ")

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as resp:
            print(resp.status)
            print(await resp.text())

if __name__ == "__main__":
    asyncio.run(main())
