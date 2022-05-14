import asyncio
from aiohttp import web


class App:
    def __init__(self):
        pass

    async def main(self, request):
        return web.Response(text='Hello, world')

    async def post_main(self, request):
        return web.Response(text='Hi, world')

    async def put_main(self, request):
        return web.Response(text='Good morning, world')

    def init_func(self):
        app = web.Application()
        app.add_routes([
            web.get('/', self.main),
            web.get('/post', self.post_main),
            web.get('/put', self.put_main)
        ])
        return app


if __name__ == '__main__':
    app = App()
    web.run_app(app.init_func())