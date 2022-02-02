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

async def print_every_5_sec(counter):
    while True:
        await asyncio.sleep(5)
        print(f'Length of counter after 5 second: {len(counter)}')

async def print_every_10_sec(counter):
    while True:
        await asyncio.sleep(10)
        print(f'Length of counter after 10 second: {len(counter)}')

async def main():
    counter = []

    tasks = [
        count(counter),
        print_every_1_sec(counter),
        print_every_5_sec(counter),
        print_every_10_sec(counter),
    ]

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())