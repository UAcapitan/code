import asyncio
from aiohttp import web


routes = web.RouteTableDef()

@routes.get('/')
async def main(request):
    return web.Response(text='Hello, world')

@routes.get('/post')
async def post_main(request):
    return web.Response(text='Hello, world')

@routes.get('/put')
async def put_main(request):
    return web.Response(text='Hello, world')


def init_func():
    app = web.Application()
    app.add_routes(routes)
    return app


web.run_app(init_func())