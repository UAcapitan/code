
import random
import asyncio


@asyncio.coroutine
def one_coroutine(name, n):
    for i in range(n):
        print(f"{name} - {str(i + 1)}")
        yield from asyncio.sleep(1)

def run(elems):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(elems)


if __name__ == "__main__":
    to_do = asyncio.wait([one_coroutine(f"Coroutine_{str(i)}", random.randint(1,7)) for i in range(7)])
    run(to_do)