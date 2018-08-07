from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)
db = client.get_default_database()
posts = db["posts"]
new_post = {
    "title": "Cổ điển",
    "author": "Tofu",
    "content": "Gió mây đưa nhẹ lay mái tóc thưa.Cốc nâu khói bay xoa bàn tay nơi góc xưa.Anh đưa em về với kiểu cũ đã cổ điển"
}
posts.insert_one(new_post)