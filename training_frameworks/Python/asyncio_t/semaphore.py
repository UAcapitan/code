import asyncio

async def printer(sem, num):
    async with sem:
        print(num)
        print(sem)
        print('Working')
        await asyncio.sleep(3)

async def main():
    # sem = asyncio.Semaphore(value=2)
    sem = asyncio.BoundedSemaphore(value=2)
    list_of_i = [printer(sem, i) for i in range(10)]
    await asyncio.wait(list_of_i)
    print('Stoped')

if __name__ == '__main__':
    asyncio.run(main())
