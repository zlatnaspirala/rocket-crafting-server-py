from pymongo import MongoClient
import config
import services.email.service as emailService
import services.email.templates as emailTemplates
SHEMA = {"DB_USER": "null"}

SHEMA["DB_USER"] = {
  "email": "fake_pythontest@localhost.com",
  "password": "",
  "nickname": "no-nick-name0",
  "confirmed": "true",
  "token": "DjoBw",
  "socketid": "null",
  "online": "false",
  "points": 525,
  "rank": "junior",
  "permission": "basic",
  "age": "any",
  "country": "any",
  "ban": "false",
  "profileUrl": "/imgs/DjoBw"
}

def RocketCraftingServer(collection):
    # print("SECRET: ")
    client = MongoClient(config.getDBAddress())
    # print(client.list_database_names()[0])
    print("Default db name:" +str(client['rocket-1']))
    return client['rocket-1'][collection]

def register(documentToInsert, collection):
    print("document,:" + documentToInsert.email )
    emailService.SEND_COMF("zlatnaspirala@gmail.com", emailTemplates.confirmationTemplate())
    try:
        collection.insert_one(documentToInsert)
        return True
    except Exception as e:
        print("An exception occurred ::", e)
        return False
