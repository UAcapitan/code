import asyncio

async def waiter(event):
    print('Waiting')
    await event.wait()
    print('End of waiting')

async def main():
    event = asyncio.Event()

    waiter_task = asyncio.create_task(waiter(event))

    await asyncio.sleep(1)
    event.set()
    
    await waiter_task

if __name__ == '__main__':
    asyncio.run(main())