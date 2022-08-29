
import asyncio
from typing import Coroutine, Generator
import aioconsole


# Generator - almost coroutine
def first() -> Generator:
    n = 0
    while True:
        yield n
        n += 1

# First coroutine
def second() -> Generator:
    list_: list = []
    while True:
        n = (yield list_)
        list_.append(n)

# Coroutine with asyncio
async def third() -> Coroutine:
    list_: list = []
    while True:
        n = (await aioconsole.ainput())
        await aioconsole.aprint(list_)
        list_.append(n)


if __name__ == "__main__":
    
    # Launch generator
    gen: Generator = first()
    print(next(gen))
    print(next(gen))
    print(next(gen))

    print()

    # Launch coroutine
    cor: Generator = second()
    next(cor)
    print(cor.send(1))
    print(cor.send(2))
    print(cor.send(3))

    print()

    # Launch coroutine with asyncio
    asyncio.run(third())