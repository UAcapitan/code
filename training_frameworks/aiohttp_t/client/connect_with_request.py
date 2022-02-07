import asyncio
import aiohttp

async def main():
    async with aiohttp.request('GET', 'http://python.org/') as request:
        print(await request.text())

asyncio.run(main())