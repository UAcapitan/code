import asyncio

async def nested():
    print(1)
    return 1

async def main():
    while True:
        task = asyncio.create_task(nested())

        await task

if __name__ == '__main__':
    asyncio.run(main())