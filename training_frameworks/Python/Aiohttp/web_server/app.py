import aiohttp
from aiohttp import web
import fcntl
import ffilib


async def index(request):
    return web.Response(text='Hello, world!')

async def page(request):
    return web.Response(text='Just a page')

async def create(request):
    return web.Response(text='This is form')


def create_app():
    app = web.Application()
    app.router.add_get("/", index)
    app.router.add_get("/page", page)
    app.router.add_get("/create", create)
    return app

app = create_app()


if __name__ == '__main__':
    web.run_app(app)