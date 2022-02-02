import asyncio
from contextvars import ContextVar

MyCounter = ContextVar('context', default=0)

async def increase():
    my_count = MyCounter.get()
    my_count += 1
    MyCounter.set(my_count)

async def main():
    while True:
        await increase()
        my_count = MyCounter.get()
        print(f'Counter: {my_count}')

        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())