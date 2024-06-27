from pymongo import MongoClient
import config

def RocketCraftingServer():
		print("get_database SECRET : ")
		CONNECTION_STRING = config.getDBAddress()
		client = MongoClient(CONNECTION_STRING)
		# print(client.list_database_names()[0])
		print(client['rocket-1'])
		# collection_name = dbname["platformetPY"]
		return client['rocket-1']

# if __name__ == "__main__":
# 		# Get the database
# 		dbname = get_database()