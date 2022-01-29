import asyncio
import aiohttp
from time import time

def write_image(data):
    filename = f'file-{int(time() * 1000)}.jpg'
    with open(filename, 'wb') as file:
        file.write(data)

async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)

async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(asyncio.create_task(fetch_content(url, session)))

        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    print(time()-t0)