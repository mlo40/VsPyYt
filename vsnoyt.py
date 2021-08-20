import asyncio
import websockets

import time

import os
import pickle

import funcv2
from funcv2 import *

from json import *

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
        while True:
            await mdmv(websocket,0.2,False,0.1,0.1,300,-22.5)
            await listArtM(websocket,255,150,0,255,True,"","","","","")
            time.sleep(0.1)
asyncio.get_event_loop().run_until_complete(main())
