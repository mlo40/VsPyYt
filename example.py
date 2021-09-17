import json
import time
import os

import setup
from setup import *

async def main():
    try:
        websocket = await websockets.connect('ws://127.0.0.1:8001')
    except:
        print("Couldn't connect to vtube studio")
        input("press enter to quit program")
        quit()
    await setup(websocket)
    while True:
asyncio.run(main())