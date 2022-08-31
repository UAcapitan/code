
import asyncio


async def counter_1(n: int) -> None:
    while True:
        print(f"Counter 1: {str(n)}")
        n += 1
        await asyncio.sleep(1)

async def counter_2(n: int) -> None:
    while True:
        print(f"Counter 2: {str(n)}")
        n += 1
        await asyncio.sleep(3)

async def counter_3(n: int) -> None:
    while True:
        print(f"Counter 3: {str(n)}")
        n += 1
        await asyncio.sleep(7)

async def main() -> None:
    await asyncio.gather(
        *[
            counter_1(1),
            counter_2(1),
            counter_3(1)
        ]
    )


if __name__ == "__main__":
    asyncio.run(main())
