import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://google.com') as resp:
            print(resp.status)

        async with session.post('http://httpbin.org/post', data=b'data') as resp:
            data = await resp.text()
            print(data)


if __name__ == "__main__":
    asyncio.run(main())