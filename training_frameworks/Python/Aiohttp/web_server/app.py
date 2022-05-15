import aiohttp
from aiohttp import web

async def create_app():
    app = web.Application()
    return app

app = create_app()

if __name__ == '__main__':
    aiohttp.web.run_app(app,)