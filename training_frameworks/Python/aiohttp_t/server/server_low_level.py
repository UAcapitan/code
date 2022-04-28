import asyncio
from aiohttp import web


async def handler(request):
    return web.Response(text='Hello, world')

async def main():
    server = web.Server(handler)
    runner = web.ServerRunner(server)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 5000)
    await site.start()

    print('Serving on 0.0.0.0:5000')

    await asyncio.sleep(100*3600)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Server was closed')