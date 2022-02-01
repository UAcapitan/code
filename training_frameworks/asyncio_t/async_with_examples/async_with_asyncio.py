import asyncio


async def counter():
    counter = 0
    while True:
        print(counter)
        counter += 1
        await delay_async()

async def printer():
    counter = 0
    while True:
        if counter % 3 == 0:
            print('Working')
        counter += 1
        await delay_async()

async def delay_async():
        await asyncio.sleep(1)

async def main():
    tasks = []
    tasks.append(asyncio.create_task(counter()))
    tasks.append(asyncio.create_task(printer()))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())