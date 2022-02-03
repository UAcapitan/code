import asyncio
from time import time

def main_usual(num):
    n = 0
    for i in range(num):
        n = (n+i)*i
    return n

async def main_async(num, nums):
    n = 0
    for i in range(num):
        n = (n+i)*i
    nums.append(n)

async def main_for_run():
    t = time()
    list_of_num = []
    await asyncio.gather(*[main_async(i, list_of_num) for i in range(300)])
    print(time() - t)

async def main_for_run_2():
    list_of_num = []
    loop = asyncio.get_event_loop()

    tasks = []

    for i in range(300):
        tasks.append(loop.create_task(main_async(i, list_of_num)))

        asyncio.gather(*tasks)
    
    # print(list_of_num)

def main():
    list_of_num = []
    for i in range(300):
        list_of_num.append(main_usual(i))
    
    # print(list_of_num)

if __name__ == '__main__':
    t = time()
    main()
    print(time() - t)

    t = time()
    asyncio.run(main_for_run_2())
    print(time() - t)