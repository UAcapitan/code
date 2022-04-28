import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession('http://python.org') as session:
        request = await session.get('/doc')
        print(f'Status: {request.status}')
        await session.close()


if __name__ == '__main__':
    asyncio.run(main())