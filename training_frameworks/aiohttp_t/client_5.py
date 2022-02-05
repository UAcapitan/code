import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com/events') as request:
            print(await request.content.read(200))
            with open('file.txt', 'wb') as file:
                async for chunk in request.content.iter_chunked(10):
                    file.write(chunk)

if __name__ == '__main__':
    asyncio.run(main())