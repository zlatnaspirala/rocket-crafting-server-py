import asyncio
import websockets
from services.utils.utils import bgcolors
import networking.net as netHandler
import json
from termcolor import colored
import config

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# RocketCraftingServerPy
# version 1.0.0
# Python vs MongoDB real powerfull choose
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


async def send_ping(websocket):
    print("Sent ping message attached.")
    while True:
        data = await websocket.recv()
        print(colored('data:', 'red'), colored(data, 'green'))
        netHandler.handleClientRequest(data, websocket)
        await asyncio.sleep(1)
        ping = {"type": "ping"}
        await websocket.send(json.dumps(ping))


async def handleClient(websocket, path):
    data = await websocket.recv()
    print("r______: " + data)
    if data == "Connection Established":
        print("<JUST WELCOME>")
        await send_ping(websocket)
        return
    # Sock draft
    await send_ping(websocket)

# Start sock server
start_server = websockets.serve(
    handleClient, config.getServerName(), config.port())

print(bgcolors.WARNING +
      "Rocket Crafting Server Py Sock started on port: " + str(config.port()))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
