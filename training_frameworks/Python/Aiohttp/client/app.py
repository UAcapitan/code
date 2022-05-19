import aiohttp
import asyncio


async def main():
    params = {"Key1": "1", "Key2": "2", "Key3":"3"}

    files = {
        'file': open('file_for_sending.py', 'rb')
    }
    data_for_file = aiohttp.FormData()
    data_for_file.add_field('file', files["file"], filename="file_for_sending.py")


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

        async with session.post(url_post, json={"text": "text"}) as resp:
            print(await resp.json())

        async with session.get(url) as resp:
            print(await resp.content.read(10))

        async with session.post(url_post, data=data_for_file) as resp:
            print(await resp.json())


if __name__ == "__main__":
    asyncio.run(main())