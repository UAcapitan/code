from aiohttp import web

async def hi(request):
    return web.Response(text='Hi, world!')

app = web.Application()
app.add_routes([web.get('/', hi)])
web.run_app(app)