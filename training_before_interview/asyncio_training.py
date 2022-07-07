import asyncio
import random

async def task():
    n = random.randint(1,11)
    while True:
        await asyncio.sleep(n)
        print(f"Success, {str(n)} seconds")

async def main():
    await asyncio.gather(*[
        task(),
        task(),
        task()
    ])

if __name__ == '__main__':
    asyncio.run(main())