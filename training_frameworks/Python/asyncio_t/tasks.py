import asyncio

async def printer(id):
    while True:
        print(f'Task {id}')
        await asyncio.sleep(1)

async def main():
    for i in range(5):
        asyncio.create_task(printer(i+1))

    print(f'Len: {len(asyncio.all_tasks()) - 1}')

    await asyncio.gather(*asyncio.all_tasks())

if __name__ == '__main__':
    asyncio.run(main())