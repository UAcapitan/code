from aiohttp import web
import aiofiles


async def main(request):
    data = await request.post()
    print(data)
    async with aiofiles.open('html_pages/form_text.html', 'rb') as fi:
        f = await fi.read()
    return web.Response(
        body=f,
        content_type='text/html',
        charset='utf-8',
        status=200
    )

async def file_page(request):
    data = await request.post()
    print(data)
    async with aiofiles.open('html_pages/form_file.html', 'rb') as fi:
        f = await fi.read()
    return web.Response(
        body=f,
        content_type='text/html',
        charset='utf-8',
        status=200
    )

async def form(request):
    data = await request.post()
    print(data)
    text = f'{data["login"]} - {data["password"]}'
    return web.Response(text=text)

async def data(request):
    data = await request.post()
    file_data = data["file"]
    text = file_data.filename
    file_readed = file_data.file.read()
    async with aiofiles.open('files/' + text, 'wb') as f:
        await f.write(file_readed)
        await f.flush()
    return web.Response(text=text)


app = web.Application()
app.add_routes([
    web.get('/', main),
    web.get('/file', file_page),
    web.post('/form', form),
    web.post('/data', data)
])


web.run_app(app, port=5000)