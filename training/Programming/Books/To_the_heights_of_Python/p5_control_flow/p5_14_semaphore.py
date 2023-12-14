
import random
import asyncio

import tqdm


async def get_page(semaphore, n):
    async with semaphore:
        await asyncio.sleep(random.randint(1,9))
        print(f"Query {str(n)}")

async def main():
    semaphore = asyncio.Semaphore(3)
    to_do = asyncio.as_completed([get_page(semaphore, i + 1) for i in range(15)])

    for td in tqdm.tqdm(to_do, total=15):
        await td


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
