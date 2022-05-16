from aiohttp import web


async def index(request):
    return web.Response(text='Hello, world!')

async def page(request):
    return web.Response(text='Just a page')

async def create(request):
    return web.Response(text='This is form')


app = web.Application()
app.router.add_get("/", index)
app.router.add_get("/page", page)
app.router.add_get("/create", create)


if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=3000)