import json
import time
import os

import setup
from setup import *

if os.path.exists('customfunc.py'):
    import customfunc
    from customfunc import *

bot='bots'

async def main():
    try:
        websocket = await websockets.connect('ws://127.0.0.1:8001')
    except:
        print("Couldn't connect to vtube studio")
        input("press enter to quit program")
        quit()
    twitch = await websockets.connect('ws://irc-ws.chat.twitch.tv:80')
    cmm = await setup(websocket)
    ###############################################
    #           platform selction, setup          #
    ###############################################
    link="https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=vpciz43dbe5tzwos67fqoyrqn618c8&redirect_uri=http://localhost&scope=chat:read+chat:edit&force_verify=true"
    with open('token.json') as json_file:
        data = json.load(json_file)
        json_file.close()
    op=input("do you want to use [1]Youtube chat, [2]Twitch chat ")
    if (op == "1"):
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
        channel=input("input channel name ")
    
    
    ###############################################
    #         Main loops for twitch and yt        #
    ###############################################
    if (op == "1"):
        while True:
            for key in data["data"]:
                while chat.is_alive():
                    for c in chat.get().sync_items():
                        p = [f"{c.datetime}", f"{c.author.name}", f"{c.message}"]
                        print(p)
                        if p[2] == key:
                            mdinf = await getmd(websocket)
                            s = mdinf["data"]["modelPosition"]["size"]
                            r = mdinf["data"]["modelPosition"]["rotation"]
                            x = mdinf["data"]["modelPosition"]["positionX"]
                            y = mdinf["data"]["modelPosition"]["positionY"]
                            cm = data["data"][key]
                            await eval(cm)
    elif (op == "2"):
        await twitch.send('PASS oauth:'+data['authenticationkeytwitch'])
        await twitch.send('NICK '+bot)
        await twitch.send('JOIN #'+channel)
        res = await twitch.recv()
        print(res)
        res = await twitch.recv()
        print(res)
        res = await twitch.recv()
        print(res)
        while True:
            res = await twitch.recv()#getting twitch chat is soo fucking easy. Parsing it is hell
            message_list = res.split(':')#thanks to elburz article:https://interactiveimmersive.io/blog/content-inputs/twitch-chat-in-touchdesigner/
            user_message = message_list[-1]
            user_name = message_list[1].split('!')[0]
            print(user_message,user_message[0:len(user_message)-2])
            for key in cmm['COMMANDS']:
                if user_message[0:len(user_message)-2] == key:
                    print('executing')
                    mdinf = await getmd(websocket)
                    s = mdinf["data"]["modelPosition"]["size"]
                    r = mdinf["data"]["modelPosition"]["rotation"]
                    x = mdinf["data"]["modelPosition"]["positionX"]
                    y = mdinf["data"]["modelPosition"]["positionY"]
                    cm = cmm['COMMANDS'][key]
                    await eval(cm)
asyncio.run(main())
