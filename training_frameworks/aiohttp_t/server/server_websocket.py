import asyncio
from aiohttp import web
import aiohttp


async def main(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'Error {ws.exception()}')

    print('Websocket connection closed')

    return ws


app = web.Application()
app.add_routes([web.get('/', main)])

web.run_app(app, port=5000)