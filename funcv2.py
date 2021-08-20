import json

dev = "emlo40"
reqid = "oof"
name = "a nock off of a cool program"
v = "1.0"

######################################
#            custom msg              #
######################################
async def detect_do(word,action,x,chat):
    if chat == word:
        action(x)

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
    authres = pack['data']
    print(authres)
    
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
    authres = pack['data']
    print(authres)

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
    print(authres)
    return authres

async def getstate(websocket):
    payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": v,
            "requestID": reqid,
            "messageType": "APIStateRequest",
        }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    authres = pack['data']
    print(authres)
    return authres

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
    authres = pack['data']
    print(authres)
    return authres

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
    authres = pack['data']
    return authres

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
    authres = pack['data']
    return authres

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
    authres = pack['data']
    return authres

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
    authres = pack['data']
    return authres
