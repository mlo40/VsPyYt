import asyncio
import websockets

import time

import os

import func
from func import *

from json import *
if os.path.exists('custom.py'):
    import customfunc
    from customfunc import *

async def main():
    uri = "ws://127.0.0.1:8001"
    async with websockets.connect(uri) as websocket:
        #################################
        #        saving code starts     #
        #################################
        if os.path.exists('tokenn.json'):
            data = json.load(open('tokenn.json'))
            if data['authenticationkey'] == "":
                print('Fetching New Tokens...')
                authtoken = await token(websocket)
                print(authtoken)
                print('Saving authtoken for Future Use...')
                json_file = open('tokenn.json', "r")
                data = json.load(json_file)
                data["authenticationkey"] = authtoken
                json_file.close()
                json_file = open('tokenn.json', "w")
                json_file.write(json.dumps(data))
                json_file.close()
            else:
                print('Loading authtoken From File...')
                with open('tokenn.json') as json_file:
                    data = json.load(json_file)
                    authtoken = (data['authenticationkey'])
                    json_file.close()
        else:
            print('Fetching New Tokens...')
            authtoken = await token(websocket)
            print(authtoken)
            print('Saving authtoken for Future Use...')
            with open('tokenn.json', "w") as json_file:
                jsonfilecon = {"authenticationkey": authtoken}
                json_file.write(json.dumps(jsonfilecon))
                json_file.close()
        #############################
        #        saving code ends   #
        #############################
        await authen(websocket,authtoken)
        while True:
            #code here
            time.sleep(0.1)
asyncio.get_event_loop().run_until_complete(main())