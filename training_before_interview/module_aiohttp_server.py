from aiohttp import web

async def hi(request):
    return web.Response(text='Hi, world!')