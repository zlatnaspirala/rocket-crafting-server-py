import asyncio
import websockets
import config
import database.db as rcs

# Run DB part
RCS = rcs.RocketCraftingServer()
print("DB->" , RCS)

# create handler for each connection
async def handler(websocket, path):
    data = await websocket.recv()
    reply = f"Recieved: {data}!"
    await websocket.send(reply + "{ai: 'na margini me potrazi'}")

print("RocketCraftingServerPy server started with " + config.getDBAddressAlias())
start_server = websockets.serve(handler, config.getServerName(), config.port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()