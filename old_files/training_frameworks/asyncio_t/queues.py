import asyncio
import random

async def news_producer(q):
    while True:
        await asyncio.sleep(1)
        print('Putting new item')
        await q.put(random.randint(1,5))

async def news_costumer(id, q):
    print(q)
    while True:
        print(f'Id: {id}')
        item = await q.get()
        if item is None:
            break
        print(f'Costumer: {item} - {id}')

async def main():
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop, maxsize=10)
    await asyncio.gather(
        news_producer(queue),
        news_costumer(1, queue),
        news_costumer(2, queue)
    )

if __name__ == '__main__':
    asyncio.run(main())