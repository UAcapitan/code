import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            print(f'Status: {response.status}')
            print(f'Headers: {response.headers["content-type"]}')
            html = await response.text()
            print(f'Body: {html[:15]} ...')


if __name__ == '__main__':
    asyncio.run(main())