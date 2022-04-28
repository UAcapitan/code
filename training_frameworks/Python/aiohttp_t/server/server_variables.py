import asyncio
from aiohttp import web


routes = web.RouteTableDef()

@routes.get('/{name}')
async def main(request):
    return web.Response(text=f'Hello, {request.match_info["name"]}')


app = web.Application()
app.add_routes(routes)

web.run_app(app, port=5000)