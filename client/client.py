#!/usr/bin/env python
# WS client example

import asyncio
import websockets
import time
import os

deployment = os.getenv('DEPLOYMENT')
uri = "ws://0.0.0.0:8890"
if deployment == "DEVELOPMENT":
    uri = "ws://websocket-server-svc:8890"
print(f"uri: {uri}")


async def hello():

    async with websockets.connect(uri) as websocket:

        await websocket.send('jude')

        greeting = await websocket.recv()
        print(f"< {greeting}")


while True:
    asyncio.get_event_loop().run_until_complete(hello())
    time.sleep(2)
