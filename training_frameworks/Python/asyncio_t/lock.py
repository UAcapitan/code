import asyncio

async def worker(lock, num):
    print(f'Start {num}')
    async with lock:
        print(f'Locked {lock}')
        await asyncio.sleep(1)
    print(f'End {num}')

async def main():
    lock = asyncio.Lock()

    await asyncio.wait([worker(lock, '1'), worker(lock, '2')])

if __name__ == '__main__':
    asyncio.run(main())