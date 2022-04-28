from aiohttp import web


async def main(request):
    return web.Response(text='Hello, world')

async def page(request):
    location = request.app.router['main'].url_for()
    return web.HTTPFound(location=location)


app = web.Application()

app.router.add_get('/', main, name='main')
app.router.add_get('/page', page)

web.run_app(app, port=5000)