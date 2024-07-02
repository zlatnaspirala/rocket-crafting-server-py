from pymongo import MongoClient
import config
import services.email.service as emailService
import services.email.templates as emailTemplates
import services.utils.utils as utils

# ~~~~~~~~~~~~~~~~~~~~~
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
