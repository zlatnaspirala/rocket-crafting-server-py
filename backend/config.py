
###################################
# RocketCraftingServer Config file
###################################
import json


def getDBAddress():
    dbAddress = "mongodb+srv://zlatnaspirala:LH39fPsBu8QVD6gw@cluster0.kft9q9e.mongodb.net/test?authSource=admin&readPreference=primary&ssl=true"
    return dbAddress


def getDBAddressAlias():
    dbAddress = "mongodb+srv://zlatnaspirala:LH39fPsBu8QVD6gw@cluster0.kft9q9e.mongodb.net/test?authSource=admin&readPreference=primary&ssl=true"
    return dbAddress


def getServerName():
    return "localhost"


def port():
    return 8000


emailService = {
    "port": 587,
    "smtp_server": "live.smtp.mailtrap.io",
    "login": "api",
    "password": "*******************",
    "sender_email": "GamePlay@maximumroulette.com",
    "receiver_email": "zlatnaspirala@gmail.com"
}
