from os import system, name
import json
import time
######################################
#          plugin settings           #
######################################
dev = "test"
reqid = "test"
name = "test"
v = "1.0"
######################################
#             functions              #
######################################

async def token(websocket):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "AuthenticationTokenRequest",
            "data": {
                "pluginName": name,
                "pluginDeveloper": dev,
            }
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    authtoken = pack['data']['authenticationToken']
    return authtoken

async def authen(websocket,authtoken):
    payload={
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "AuthenticationRequest",
            "data": {
                "pluginName": name,
                "pluginDeveloper": dev,
                "authenticationToken": authtoken
            }
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack

async def gettrackparam(websocket):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "InputParameterListRequest"
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack

async def getmd(websocket):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "CurrentModelRequest"
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack

async def listvtsmodel(websocket):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "AvailableModelsRequest"
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack

async def getapi(websocket):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "APIStateRequest",
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack

async def getstat(websocket):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "StatisticsRequest"
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack

async def getvtsfolder(websocket):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "VTSFolderInfoRequest"
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    authres = pack['data']
    return pack

async def gethotkeys(websocket,mdid):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "HotkeysInCurrentModelRequest",
            "data": {
                "modelID": mdid,
            }
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack

async def mdch(websocket,mdid):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "ModelLoadRequest",
            "data": {
                "modelID": mdid
                }
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack

async def mdmv(websocket,time,revelance,xp,yp,rot,size):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "MoveModelRequest",
            "data": {
                "timeInSeconds": time,
                "valuesAreRelativeToModel": revelance,
                "positionX": xp,
                "positionY": yp,
                "rotation": rot,
                "size": size
            }
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack

async def listArtM(websocket,mdid):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "SomeID",
            "messageType": "ArtMeshListRequest"
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack

async def TintArtM(websocket,r,g,b,a,tintall,num,exactarray,conarray,tagexactarray,tagconarray):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "ColorTintRequest",
            "data": {
                "colorTint": {
                    "colorR": r,
                    "colorG": g,
                    "colorB": b,
                    "colorA": a
                },
                "artMeshMatcher": {
                    "tintAll": tintall,
                    "artMeshNumber": num,
                    "nameExact": exactarray,
                    "nameContains": conarray,
                    "tagExact": tagexactarray,
                    "tagContains": tagconarray
                }
            }
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    return pack
    


async def spin(websocket,x,y,s):
    await mdmv(websocket,0.2,False,x,y,90,s)
    time.sleep(0.1)
    await mdmv(websocket,0.2,False,x,y,180,s)
    time.sleep(0.1)
    await mdmv(websocket,0.2,False,x,y,270,s)
    time.sleep(0.1)
    await mdmv(websocket,0.2,False,x,y,360,s)
    time.sleep(0.1)

async def rainbow(websocket):
    await TintArtM(websocket,255,0,0,255,True,"","","","","")
    time.sleep(0.2)
    await TintArtM(websocket,255,127,0,255,True,"","","","","")
    time.sleep(0.2)
    await TintArtM(websocket,255,255,0,255,True,"","","","","")
    time.sleep(0.2)
    await TintArtM(websocket,0,255,0,255,True,"","","","","")
    time.sleep(0.2)
    await TintArtM(websocket,0,0,255,255,True,"","","","","")
    time.sleep(0.2)
    await TintArtM(websocket,46,43,95,255,True,"","","","","")
    time.sleep(0.2)
    await TintArtM(websocket,139,0,255,255,True,"","","","","")
    time.sleep(0.2)
    await TintArtM(websocket,255,255,255,255,True,"","","","","")
