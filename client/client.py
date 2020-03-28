#!/usr/bin/env python
# WS client example

import asyncio
import websockets
import time

async def hello():
    uri = "ws://0.0.0.0:8890"
    async with websockets.connect(uri) as websocket:

        await websocket.send('jude')
        # print(f"> jude")

        greeting = await websocket.recv()
        print(f"< {greeting}")



while True:
    asyncio.get_event_loop().run_until_complete(hello())
    time.sleep(2)