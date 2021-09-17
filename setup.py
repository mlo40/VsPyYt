import os
import json
import configparser

import asyncio
import websockets

import func
from func import *

import pytchat
from pytchat import *
import webbrowser
async def setup(websocket):
    if os.path.exists('token.json'):
        print('Loading authtoken From File...')
        with open('token.json', "r") as json_file:
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
                            "chatspeed": 0.1,
                            "authenticationkey": authtoken,
                            "authenticationkeytwitch": ""
                        }
                json_file.write(json.dumps(jsonfilecon))
                json_file.close()
            await authen(websocket,authtoken)
    if os.path.exists('commands.ini'):
        config = configparser.ConfigParser()
        cmm = config.read('commands.ini')
    else:
        config = configparser.ConfigParser()
        with open('commands.ini', "w") as configfile:
            config['COMMANDS'] = {
                    "!spin": "spin(websocket,x,y,s)",
                    "!reset": "mdmv(websocket,0.2,False,0,0,0,-76)",
                    "!rainbow": "rainbow(websocket)"
                }
            config.write(configfile)
    with open('token.json') as json_file:
        data = json.load(json_file)
        json_file.close()
    ###############################
    #   command auto generation   #
    ###############################
    mdls = await listvtsmodel(websocket)
    runs = mdls["data"]["numberOfModels"]
    i=0
    for key in config['COMMANDS']:
        i+=1
    nmumm = runs - i
    if i < nmumm:
        with open('commands.ini', "w") as configfile:
            for i in range(runs):
                ff = mdls["data"]["availableModels"][i]["modelName"]
                gg = mdls["data"]["availableModels"][i]["modelID"]
                name = "!"+ff
                mdss = mdch.__name__+"("+"websocket"+",'"+str(gg)+"')"
                config['COMMANDS'][name] = mdss
            config.write(configfile)
        ###############################
        # command auto generation end #
        ###############################
    print("Successfully Loaded")
    print("Detected Commands")
    for key in config['COMMANDS']:
        print(key)
    return config
async def qa():
    link="https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=vpciz43dbe5tzwos67fqoyrqn618c8&redirect_uri=http://localhost&scope=chat:read+chat:edit&force_verify=true"
    yt = False
    ttv = False
    chat=None
    chnm=None
    with open('token.json') as json_file:
        data = json.load(json_file)
        json_file.close()
    op=input("do you want to use [1]Youtube chat, [2]Twitch chat ")
    if (op == "1"):
        yt = True
        op=input("input streamid ")
        chat = LiveChat(video_id=op)
    elif (op == "2"):
        if (data['authenticationkeytwitch'] == ''):
            print("click authorize, copy the token from access_token=, till the & seperator")
            webbrowser.open(link)
            twauthtoken = input()
            with open('token.json', "w") as json_file:
                data["authenticationkeytwitch"] = twauthtoken
                json_file.write(json.dumps(data))
                json_file.close()
            data = json.load(open('token.json'))
            json_file.close()
        ttv = True
        chnm=input("input channel name ")
    return [yt,ttv,data,chat,chnm]