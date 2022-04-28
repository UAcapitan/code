import asyncio
import aiohttp


async def main():
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get('http://httpbin.org/get') as request:
            print(await request.text())
    print('Task is ended')


if __name__ == '__main__':
    asyncio.run(main())        