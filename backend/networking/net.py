# Net handler
import database.db as rcs
import json

def handleClientRequest(data, websocket):
    print("handleClientRequest____: " + data)
    o = json.loads(data)
    print("handleClientRequest____: " + o["action"] )

    if str(o["action"]) == "REGISTER":
        print("<REGISTER>")
        # Run DB part test
        rcsUsers = rcs.RocketCraftingServer("users")
        rcs.SHEMA["DB_USER"]["email"] = o["userRegData"]["email"]
        rcs.SHEMA["DB_USER"]["password"] = o["userRegData"]["password"]
        result = rcs.register(rcs.SHEMA["DB_USER"], rcsUsers)
        print("REG RES -> ", result)
        rocket_send(websocket, result)
        return result;
    else:
        return "unhandled"
        print("unhandled request...")

async def rocket_send(websocket, result):
    await websocket.send(result)
    print("Sent ping message attached.")