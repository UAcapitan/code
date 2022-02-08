import asyncio
from aiohttp import web


routes = web.RouteTableDef()

@routes.get('/', name='main')
async def main(request):
    return web.Response(text=f'Hello, world')

@routes.get('/resources')
async def resources(request):
    url = request.app.router['main'].url_for().with_query({'a': 'b', 'c': 'd'})
    return web.Response(text=str(url))

@routes.get('/user-data')
async def user_data(request):
    url = request.app.router['user_info'].url_for(user='TestUserNew').with_query(
        {'a':'b', 'c': 'd'}
    )
    return web.Response(text=str(url))


app = web.Application()
app.add_routes(routes)
app.router.add_resource(r'/user/{user}/info', name='user_info')

web.run_app(app, port=5090)