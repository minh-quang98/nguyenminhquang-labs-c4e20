from pymongo import MongoClient
mongo_uri = "mongodb://admin:123abc@ds033477.mlab.com:33477/c4e20_lab"

# 1 connect to database
client = MongoClient(mongo_uri)

# 2 get database
db = client.get_default_database()

# 3 create a collection
games = db['games']

# # 4 create a document
# new_game = {
#     "title": "PES",
#     "description": "Pro evolution soccer"
# }

# # 5 insert doc into collection
# games.insert_one(new_game)

# 6 Read all documents
all_game = games.find()
first_game = all_game[0]
print(first_game['title'])