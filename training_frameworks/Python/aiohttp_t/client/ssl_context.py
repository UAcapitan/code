import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        try:
            request = await session.get('https://expired.badssl.com/', ssl=True)
            print(await request.text())
        except aiohttp.ClientConnectorSSLError as e:
            print(e)

if __name__ == '__main__':
    asyncio.run(main())