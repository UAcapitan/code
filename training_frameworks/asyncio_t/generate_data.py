import asyncio
from time import time

async def generate(name, num):
    print(f'{name} start calculation')
    n = 0
    for i in range(num):
        n = (n + i)*i
        print(f'Task {name}: {n}')
        await asyncio.sleep(0.1)
    return n

async def main():
    list_of_nums = await asyncio.gather(
        generate('Function 1', 1),
        generate('Function 2', 2),
        generate('Function 3', 14),
        generate('Function 4', 5),
        generate('Function 5', 3),
        generate('Function 6', 4),
        generate('Function 7', 5),
    )

    print(list_of_nums)

if __name__ == '__main__':
    t = time()
    asyncio.run(main())
    print(time() - t)