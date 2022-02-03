import asyncio

async def words(time, text):
    await asyncio.sleep(time)
    print(text)

async def main():
    await asyncio.gather(
        words(10,'New'),
        words(5,'Text'),
        words(7,'Test'),
        words(12,'Code'),
        words(30,'Words'),
        words(5,'Something'),
        words(1,'Time'),
    )

if __name__ == '__main__':
    asyncio.run(main())