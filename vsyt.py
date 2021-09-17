import json
import time
import os

import setup
from setup import *
bot='bots'
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
    twitch = await websockets.connect('ws://irc-ws.chat.twitch.tv:80')
    cmm = await setup(websocket)
    setus = await qa()
    yt = setus[0]
    ttv = setus[1]
    data = setus[2]
    chat = setus[3]
    channel = setus[4]
    if (yt == True):
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
    elif (ttv == True):
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
            res = await twitch.recv()#getting twitch chat is soo fucking easy
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
