import asyncio

async def count(counter):
    print(f'Length of counter: {len(counter)}')

    while True:
        await asyncio.sleep(1 / 1000)
        counter.append(1)

async def print_every_1_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'Length of counter after 1 second: {len(counter)}')