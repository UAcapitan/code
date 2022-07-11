from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def hi(request):
    return web.Response(text='Hi, world!')

app = web.Application()
app.add_routes(routes)
web.run_app(app)