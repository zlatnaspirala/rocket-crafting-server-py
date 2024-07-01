# Net handler
import database.db as rcs
import json

def handleClientRequest(data):
    print("handleClientRequest____: " + data)
    NIK = json.loads(data)
    print("handleClientRequest____: " + NIK["action"] )
    
    if str(NIK["action"]) == "REGISTER":
        print("REGISTER CALL: ")
        # Run DB part test
        rcsUsers = rcs.RocketCraftingServer("users")
        rcs.SHEMA["DB_USER"]["email"] = data["userRegData"]["email"]
        rcs.SHEMA["DB_USER"]["password"] = data["userRegData"]["password"]
        rcs.register(rcs.SHEMA["DB_USER"], rcsUsers)
        print("rcsUsers -> ", rcsUsers)