from pymongo import MongoClient
import config
import services.email.service as emailService
import services.email.templates as emailTemplates
import services.utils.utils as utils

# ----------------------------------------------------
# DATABASE SCRIPT
# Basic session operation (reg, confirm, login ...)
# ----------------------------------------------------

crypto_handler = utils.CryptoHandler()

SHEMA = {"DB_USER": "null"}

SHEMA["DB_USER"] = {
    "email": "fake_pythontest@localhost.com",
    "password": "",
    "nickname": "no-nick-name0",
    "confirmed": False,
    "token": "aaaaaa",
    "socketid": "null",
    "online": False,
    "points": 1000,
    "rank": "junior",
    "permission": "basic",
    "age": "any",
    "country": "any",
    "ban": "false",
    "profileUrl": "/imgs/default"
}


def RocketCraftingServer(collection):
    # print("SECRET: ")
    client = MongoClient(config.getDBAddress())
    # print(client.list_database_names()[0])
    print("Default db name:" + str(client['rocket-1']))
    return client['rocket-1'][collection]


def register(documentToInsert, collection):
    print("register : " + documentToInsert["email"])
    try:
        test = collection.find_one({"email": documentToInsert["email"]})
        if test == None:
            test = crypto_handler.encrypt(str(documentToInsert["password"]))
            documentToInsert["password"] = test
            documentToInsert["token"] = utils.GetToken()
            emailService.SEND_COMF(documentToInsert["email"], emailTemplates.confirmationTemplate(
                documentToInsert["token"], documentToInsert["email"]))
            collection.insert_one(documentToInsert)
            return "OK"
        else:
            # Already registred!
            print("Already registred! ", test["email"])
            return "Already Registred"
    except Exception as e:
        print("An exception occurred ::", e)
        return False


def registerConfirmation(documentToInsert, collection):
    print("documentToInsert.email : " + str(documentToInsert["email"]))
    try:
        test = collection.find_one(
            {"email": documentToInsert["email"], "token": documentToInsert["token"]})
        if test == None:
            print("NO_CONFIRMATION : ", str(documentToInsert["token"]))
            return "NO_CONFIRMATION"
        else:
            # Already registred now confirm!
            test = collection.update_one({"email": documentToInsert["email"], "token": documentToInsert["token"]},
                                         {"$set": {'confirmed': True}})
            print("Confirmed registred! ", test)
            return "USER_CONFIRMED"
    except Exception as e:
        print("An exception occurred ::", e)
        return False


def login(documentToInsert, collection):
    print("login fоr email: " + str(documentToInsert["email"]))
    try:
        testPass = collection.find_one({"email": documentToInsert["email"]})
        if testPass != None:
            print("SIFRA -> ", testPass['password'])
            print("SIFRA -> ", crypto_handler.decrypt(testPass['password']))
            original_pass = crypto_handler.decrypt(testPass['password'])
            if str(documentToInsert["password"]) == original_pass:
                print("<LOGIN PASSED>")
                user = collection.update_one({"email": documentToInsert["email"], "token": testPass['token']},
                                             {"$set": {'online': True}})
                # SEC
                userData = {
                    "email": testPass["email"],
                    "nickname": testPass["nickname"],
                    "confirmed": testPass["confirmed"],
                    "token": testPass["token"],
                    # "socketid":: user["email"],
                    "online": testPass["online"],
                    "points": testPass["points"],
                    "rank": testPass["rank"],
                    "permission": testPass["permission"],
                    "age": testPass["age"],
                    "country": testPass["country"],
                    "ban": testPass["ban"],
                    "profileUrl": testPass["profileUrl"]}
                return {"message": "You logged.",
                        "rocketStatus": "USER_LOGGED",
                        "flag": userData}
            else:
                return "NO_LOGIN"
        else:
            return "NO_LOGIN"
    except Exception as e:
        print("An exception occurred ::", e)
        return False


def fastLogin(documentToInsert, collection):
    print("fastlogin work only if online is true fоr user/email: " +
          str(documentToInsert["email"]))
    try:
        testPass = collection.find_one({
            "email": documentToInsert["email"],
            "token": documentToInsert["token"],
            "online": True})
        if testPass != None:
            print("token access -> ", testPass['token'])
            print("<FASTLOGIN PASSED>")
            # SEC
            userData = {
                "email": testPass["email"],
                "nickname": testPass["nickname"],
                "confirmed": testPass["confirmed"],
                "token": testPass["token"],
                # "socketid":: user["email"],
                "online": testPass["online"],
                "points": testPass["points"],
                "rank": testPass["rank"],
                "permission": testPass["permission"],
                "age": testPass["age"],
                "country": testPass["country"],
                "ban": testPass["ban"],
                "profileUrl": testPass["profileUrl"]}
            return {"message": "You logged.",
                    "rocketStatus": "USER_LOGGED",
                    "flag": userData}
        else:
            return "NO_LOGIN"
    except Exception as e:
        print("An exception occurred ::", e)
        return False


def logout(documentToInsert, collection):
    print("logout :" + str(documentToInsert["email"]))
    try:
        testPass = collection.find_one({
            "email": documentToInsert["email"],
            "token": documentToInsert["token"],
            "online": True})
        if testPass != None:
            print("token access -> ", testPass['token'])
            print("<FASTLOGIN PASSED>")
            user = collection.update_one({"email": documentToInsert["email"], "token": testPass['token']},
                                         {"$set": {'online': False}})
            print("USER LOGOUT ", user)
            return {"message": "Your account session is closed.",
                    "rocketStatus": "USER_LOGOUT"}
        else:
            return {"message": "Error in USER_LOGOUT.",
                    "rocketStatus": "USER_LOGOUT_ERROR"}
    except Exception as e:
        print("An exception occurred ::", e)
        return False
