import asyncio

async def waiter(event):
    print('Waiting')
    await event.wait()
    print('End of waiting')

async def main():
    event = asyncio.Event()

    waiter_task_1 = asyncio.create_task(waiter(event))
    waiter_task_2 = asyncio.create_task(waiter(event))

    await asyncio.sleep(1)
    event.set()
    
    await asyncio.gather(
        waiter_task_1,
        waiter_task_2
    )

if __name__ == '__main__':
    asyncio.run(main())