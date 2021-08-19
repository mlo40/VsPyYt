import json

dev = "emlo40"
reqid = "Owo"
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