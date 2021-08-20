import asyncio
import websockets

import time

import os

import funcv2
from funcv2 import *

from json import *

import pytchat
from pytchat import *

async def main():
    uri = "ws://127.0.0.1:8001"
    async with websockets.connect(uri) as websocket:
        if os.path.exists('token.json'):
            print('Loading authtoken From File...')
            with open('token.json') as json_file:
                data = json.load(json_file)
                streamid = (data[0]['streamid'])
                authtoken = (data[1]['authenticationkey'])
        else:
            print('Fetching New Tokens...')
            authtoken = await token(websocket)
            print(authtoken)
            print('Saving authtoken for Future Use...')
            with open('token.json', "w") as json_file:
                jsonfilecon = [{"streamid": ""},{"authenticationkey": authtoken}]
                json_file.write(json.dumps(jsonfilecon))
                #json.dump(authtoken, json_file)
        await authen(websocket,authtoken)
        chat = LiveChat(video_id=streamid)
        while True:
            for c in chat.get().sync_items():
                print(f"{c.message}")
                if "!cat" == f"{c.message}":
                    await mdch(websocket,"dfa26101c6b5471fb3694be05cb1ad97")
                elif "!human" == f"{c.message}":
                    await mdch(websocket,"ab930f0b623946abbe7db51fefcea118")
            #await getmd(websocket)
            time.sleep(0.5)
asyncio.get_event_loop().run_until_complete(main())
