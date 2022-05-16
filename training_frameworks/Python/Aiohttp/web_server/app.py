from aiohttp import web
import aiohttp_jinja2
import jinja2
from aiohttp_jinja2 import template

@template('index.html')
async def index(request):
    return {}

@template('page.html')
async def page(request):
    return {}

@template('create.html')
async def create(request):
    return {}

@template('create.html')
async def create_post(request):
    return {}

@template('success.html')
async def success(request):
    return {}


def app_launch():
    app = web.Application()

    add_jinja(app)

    all_routes(app)

    return app

def add_jinja(app):
    aiohttp_jinja2.setup(app,
        loader = jinja2.PackageLoader('app', 'templates')
    )

def all_routes(app):
    app.router.add_get("/", index)
    app.router.add_get("/page", page)
    app.router.add_get("/create", create)
    app.router.add_post("/create", create_post)
    app.router.add_get("/success", success)

if __name__ == '__main__':
    web.run_app(app_launch(), host='127.0.0.1', port=3000)