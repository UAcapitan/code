
import sys
import random
import asyncio
import warnings
from aiohttp import web

warnings.filterwarnings("ignore")


async def home(request):
    await asyncio.sleep(random.randint(1,9))
    print("Status 200: Page was loaded.")
    return web.Response(text="Hi, world!")

async def init(loop, address, port):
    app = web.Application()
    app.router.add_route("GET", "/", home)
    handler = app.make_handler()

    server = await loop.create_server(handler, address, port)
    return server.sockets[0].getsockname()

def main(address="127.0.0.1", port=2323):
    port = int(port)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    host = loop.run_until_complete(init(loop, address, port))

    print(f"Serving on {host}. Press CTRL-C to stop.")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    print("Server shutting down")
    loop.close()


if __name__ == "__main__":
    main(*sys.argv[1:])
