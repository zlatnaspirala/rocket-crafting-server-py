# Net handler
import database.db as rcs
import json


async def handleClientRequest(data, websocket):
    print("handleClientRequest____: " + data)
    o = json.loads(data)
    # print("handleClientRequest action: " + o["action"])
    if str(o["action"]) == "REGISTER":
        print("<REGISTER>")
        # Run DB part test
        rcsUsers = rcs.RocketCraftingServer("users")
        rcs.SHEMA["DB_USER"]["email"] = o["userRegData"]["email"]
        rcs.SHEMA["DB_USER"]["password"] = o["userRegData"]["password"]
        result = rcs.register(rcs.SHEMA["DB_USER"], rcsUsers)
        print("REG RES -> ", result)
        if result == "Already Registred":
            response = {
                "message": "Already Registred.",
                "rocketStatus": "Already Registred"}
            await rocket_send(websocket, json.dumps(response))
        elif result == "OK":
            response = {
                "message": "Check your email for confirmation code.",
                "rocketStatus": "CHECK_EMAIL"}
            await rocket_send(websocket, json.dumps(response))
        return result
    elif str(o["action"]) == "COMFIRMATION":
        print("<COMFIRMATION>")
        rcsUsers = rcs.RocketCraftingServer("users")
        result = rcs.registerConfirmation(o["userRegData"], rcsUsers)
        print("USER_CONFIRMED ", result)
        if result == "USER_CONFIRMED":
            response = {
                "message": "Confirmation done.",
                "rocketStatus": "USER_CONFIRMED"}
            await rocket_send(websocket, json.dumps(response))
    else:
        return "unhandled"
        print("unhandled request...")


async def rocket_send(websocket, result):
    print("Sent ping message attached.")
    await websocket.send(result)
    print("Sent ping message attached.")
