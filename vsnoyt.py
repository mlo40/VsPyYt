import json
import time
import os

import setup
from setup import *

if os.path.exists('custom.py'):
    import customfunc
    from customfunc import *

async def main():
    try:
        websocket = await websockets.connect('ws://127.0.0.1:8001')
    except:
        print("Couldn't connect to vtube studio")
        input("press enter to quit program")
        quit()
    commandlist = await setup(websocket)
    while True:
        word = input("enter command ")
        for key in commandlist['COMMANDS']:
            if word == key:
                print('executing')
                mdinf = await getmd(websocket)
                s = mdinf["data"]["modelPosition"]["size"]
                r = mdinf["data"]["modelPosition"]["rotation"]
                x = mdinf["data"]["modelPosition"]["positionX"]
                y = mdinf["data"]["modelPosition"]["positionY"]
                cm = commandlist['COMMANDS'][key]
                await eval(cm)
asyncio.run(main())