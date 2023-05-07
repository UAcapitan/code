
import sys
import random
import asyncio


query = 0

async def printer(reader, writer):
    global query
    query += 1
    n = query

    print(f"Query {str(n)}: Processing...")
    writer.write(bytes(f"Query {str(n)}: Processing...\n", encoding="utf-8"))
    await writer.drain()
    data = (await reader.readline()).decode("utf-8").strip()

    await asyncio.sleep(random.randint(1,9))
    print(f"Query {str(n)}: Response: {data}")
    writer.write(bytes(f"Query {str(n)}: Response: ({data})\n", encoding="utf-8"))
    await writer.drain()

    writer.close()

def main(address="127.0.0.1", port=2323):
    port = int(port)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    server_coro = asyncio.start_server(printer, address, port)

    server = loop.run_until_complete(server_coro)

    host = server.sockets[0].getsockname()

    print(f"Serving on {host}. Press CTRL-C to stop.")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    print("Server shutting down")
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    main(*sys.argv[1:])
