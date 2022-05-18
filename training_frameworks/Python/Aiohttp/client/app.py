import aiohttp
import asyncio


async def main():
    params = {"Key1": "1", "Key2": "2", "Key3":"3"}

    async with aiohttp.ClientSession() as session:
        async with session.get('https://google.com') as resp:
            print(resp.status)

        async with session.post('http://httpbin.org/post', data=b'data') as resp:
            data = await resp.text()
            print(data)

        url = 'https://httpbin.org/get'
        url_post = 'https://httpbin.org/post'

        async with session.get(url, params=params) as resp:
            print(resp.url) 

        async with session.get(url_post, json={"text": "text"}) as resp:
            print(await resp.json())


if __name__ == "__main__":
    asyncio.run(main())