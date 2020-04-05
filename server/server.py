#!/usr/bin/env python

# WS server example

import asyncio
import websockets


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)

start_server = websockets.serve(hello, "localhost", 8890)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
