
import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print("< " + message)
        response = "Hello, user!"
        await websocket.send(response)
        print("> " + response)

async def main():
    async with websockets.serve(echo, "127.0.0.1", 5000) as websocket:
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())