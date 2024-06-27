
###################################
# RocketCraftingServer Config file
###################################

def getDBAddress():
		dbAddress = "mongodb+srv://zlatnaspirala:**********@cluster0.kft9q9e.mongodb.net/test?authSource=admin&readPreference=primary&ssl=true"
		return dbAddress

def getDBAddressAlias():
		dbAddress = "mongodb+srv://zlatnaspirala:********@cluster0.kft9q9e.mongodb.net/test?authSource=admin&readPreference=primary&ssl=true"
		return dbAddress

def getServerName():
		return "localhost"

def port():
		return 8000

print("RocketCraftingServerPy server config")
