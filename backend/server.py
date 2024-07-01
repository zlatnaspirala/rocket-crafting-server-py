import asyncio
import websockets
import config
import networking.net as netHandler
# import database.db as rcs
import json
# RocketCraftingServerPy
# version 1.0.0

# # Run DB part test
# rcsUsers = rcs.RocketCraftingServer("users")
# rcs.register(rcs.SHEMA["DB_USER"], rcsUsers)
# print("rcsUsers->", rcsUsers)
# Sock

async def send_ping(websocket):
    print("Sent ping message attached.")
    while True:
        data = await websocket.recv()
        print('MY DATA' + data)
        netHandler.handleClientRequest(data)
        await asyncio.sleep(1)
        ping = {"type": "ping"}
        await websocket.send(json.dumps(ping))
        # print("Sent ping message")


async def handleClient(websocket, path):
    data = await websocket.recv()
    print("r______: " + data)
    if data == "Connection Established":
        print("JUST WELCOME RETURN: ")
        await send_ping(websocket)
        return
    # Sock draft
    await send_ping(websocket)

# Start sock server
start_server = websockets.serve(
    handleClient, config.getServerName(), config.port())

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

print("Rocket Crafting Server Py Sock started on port {config.port()}")
