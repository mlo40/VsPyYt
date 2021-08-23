import asyncio
import websockets

import time

import os

import func
from func import *

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
                jsonfilecon = [{"authenticationkey": authtoken}]
                json_file.write(json.dumps(jsonfilecon))
                #json.dump(authtoken, json_file)
        await authen(websocket,authtoken)
        while True:
            ###########
            #code here#
            ###########
            time.sleep(0.1)
asyncio.get_event_loop().run_until_complete(main())
