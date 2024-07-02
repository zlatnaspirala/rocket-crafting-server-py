from pymongo import MongoClient
import config
import services.email.service as emailService
import services.email.templates as emailTemplates
import services.utils.utils as utils

#~~~~~~~~~~~~~~~~~~~~~
crypto_handler = utils.CryptoHandler()

SHEMA = {"DB_USER": "null"}

SHEMA["DB_USER"] = {
  "email": "fake_pythontest@localhost.com",
  "password": "",
  "nickname": "no-nick-name0",
  "confirmed": True,
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
    print("Default db name:" +str(client['rocket-1']))
    return client['rocket-1'][collection]

def register(documentToInsert, collection):
    print("documentToInsert.email : " + documentToInsert["email"])
    try:
        test = collection.find_one({"email": documentToInsert["email"] })
        if test == None:
            print("Encode pass [str(documentToInsert[password])] : ", str(documentToInsert["password"]))
            test = crypto_handler.encrypt(str(documentToInsert["password"]))
            print("Encode pass: ", test)
            documentToInsert["password"] = test
            documentToInsert["token"] = utils.GetToken()
            emailService.SEND_COMF(documentToInsert["email"], emailTemplates.confirmationTemplate(documentToInsert["token"], documentToInsert["email"]))
            collection.insert_one(documentToInsert)
            return "OK"
        else:
            #Already registred!
            print("Already registred! ", test["email"])
            return "Already Registred"
    except Exception as e:
        print("An exception occurred ::", e)
        return False
