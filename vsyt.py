import asyncio
import websockets

import time

import os

import func
from func import *

from json import *

import pytchat
from pytchat import *

if os.path.exists('custom.py'):
    import customfunc
    from customfunc import *

async def main():
    uri = "ws://127.0.0.1:8001"
    async with websockets.connect(uri) as websocket:
        #################################
        #        saving code starts     #
        #################################
        if os.path.exists('token.json'):
            data = json.load(open('token.json'))
            if data['authenticationkey'] == "":
                print('Fetching New Tokens...')
                authtoken = await token(websocket)
                print(authtoken)
                print('Saving authtoken for Future Use...')
                json_file = open('token.json', "r")
                data = json.load(json_file)
                data["authenticationkey"] = authtoken
                json_file.close()
                json_file = open('token.json', "w")
                json_file.write(json.dumps(data))
                json_file.close()
            else:
                print('Loading authtoken From File...')
                with open('token.json') as json_file:
                    data = json.load(json_file)
                    authtoken = (data['authenticationkey'])
                    json_file.close()
        else:
            print('Fetching New Tokens...')
            authtoken = await token(websocket)
            print(authtoken)
            print('Saving authtoken for Future Use...')
            with open('token.json', "w") as json_file:
                jsonfilecon = {
                            "authenticationkey": authtoken,
                            "data":{
                                "!spin": "spin(websocket,x,y,s)",
                                "!rainbow": "rainbow(websocket)"}
                        }
                json_file.write(json.dumps(jsonfilecon))
                json_file.close()
        await authen(websocket,authtoken)
        mdls = await listvtsmodel(websocket)
        runs = mdls["data"]["numberOfModels"]
        data = json.load(open('token.json'))
        i=0
        for key in data["data"]:
            i+=1
        nmumm = runs - i
        if i < nmumm:
            for i in range(runs):
                ff = mdls["data"]["availableModels"][i]["modelName"]
                gg = mdls["data"]["availableModels"][i]["modelID"]
                json_file.close()
                name = "!"+ff
                
                mdss = mdch.__name__+"("+"websocket"+",'"+str(gg)+"')"
                data["data"][name] = mdss
                json_file.close()
                json_file = open('token.json', "w")
                json_file.write(json.dumps(data))
                json_file.close()
        #############################
        #        saving code ends   #
        #############################
        for key in data["data"]:
            print(key)
        print("type your streamid and press enter")
        streamid = input()
        chat = LiveChat(video_id=streamid)
        while True:
            mdinf = await getmd(websocket)
            s = mdinf["data"]["modelPosition"]["size"]
            x = mdinf["data"]["modelPosition"]["positionX"]
            y = mdinf["data"]["modelPosition"]["positionY"]
            json_file = open('token.json')
            data = json.load(json_file)
            for c in chat.get().sync_items():
                print(f"{c.message}")
                time.sleep(0.1)
                for key in data["data"]:
                    if f"{c.message}" == key:
                        cm = data["data"][key]
                        await eval(cm)
            time.sleep(0.1)
asyncio.get_event_loop().run_until_complete(main())
