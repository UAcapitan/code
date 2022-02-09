from aiohttp import web

async def main(request):
    api_dict = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }
    return web.json_response(api_dict)

app = web.Application()
app.add_routes([
    web.get('/', main)
])

web.run_app(app)