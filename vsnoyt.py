import asyncio
import websockets

import time

import os

import func
from func import *

import json

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
            print('Loading authtoken From File...')
            json_file = open('token.json', "r")
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
                json_file = open('token.json', "w")
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
            with open('token.json', "w") as json_file:
                jsonfilecon = {
                            "authenticationkey": authtoken,
                            "data":{
                                "!spin": "spin(websocket,x,y,s)",
                                "!reset": "mdmv(websocket,0.2,False,0,0,0,-76)",
                                "!rainbow": "rainbow(websocket)"}
                        }
                json_file.write(json.dumps(jsonfilecon))
                json_file.close()
            await authen(websocket,authtoken)
        ###############################
        #      saving code ends       #
        ###############################
        ###############################
        #   command auto generation   #
        ###############################
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
                name = "!"+ff
                mdss = mdch.__name__+"("+"websocket"+",'"+str(gg)+"')"
                data["data"][name] = mdss
                json_file.close()
                json_file = open('token.json', "w")
                json_file.write(json.dumps(data))
                json_file.close()
        ###############################
        # command auto generation end #
        ###############################
        print("Successfully Loaded")
        print("Detected Commands")
        for key in data["data"]:
            print(key)
        while True:
            word = input("enter command ")
            json_file = open('token.json')
            data = json.load(json_file)
            if word == "exit":
                    quit()
            for key in data["data"]:
                #print(key)
                if word == key:
                    mdinf = await getmd(websocket)
                    s = mdinf["data"]["modelPosition"]["size"]
                    r = mdinf["data"]["modelPosition"]["rotation"]
                    x = mdinf["data"]["modelPosition"]["positionX"]
                    y = mdinf["data"]["modelPosition"]["positionY"]
                    cm = data["data"][key]
                    await eval(cm)
            time.sleep(0.1)
asyncio.get_event_loop().run_until_complete(main())