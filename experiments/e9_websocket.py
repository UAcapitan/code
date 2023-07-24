
import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://127.0.0.1:5000") as websocket:
        await websocket.send(input("> "))
        print("< " + await websocket.recv())

if __name__ == "__main__":
    asyncio.run(hello())
