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
            print('Loading authtoken From File...')
            json_file = open('tokenn.json', "r")
            data = json.load(json_file)
            authtoken = (data['authenticationkey'])
            confirm = await authen(websocket,authtoken)
            if authtoken == "" or confirm["data"]["authenticated"] == False:
                print('Error Token Invalid')
                print('Fetching New Tokens...')
                authtoken = await token(websocket)
                print(authtoken)
                print('Saving authtoken for Future Use...')
                data["authenticationkey"] = authtoken
                json_file.close()
                json_file = open('tokenn.json', "w")
                json_file.write(json.dumps(data))
                json_file.close()
                print("Saving finished")
            else:
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
            await authen(websocket,authtoken)
        #############################
        #        saving code ends   #
        #############################
        print("Successfully Loaded")
        while True:
            #code here
            time.sleep(0.1)
asyncio.get_event_loop().run_until_complete(main())