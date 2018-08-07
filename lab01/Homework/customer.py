from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()
customers = db["customers"]
all_cus = customers.find()
eve = 0
ads = 0
wom = 0
for i in range(6969):
    cus = all_cus[i]
    if cus["ref"] == "events":
        eve += 1
    elif cus["ref"] == "ads":
        ads += 1
    elif cus["ref"] == "wom":
        wom += 1
labels = [ "events", "advertisements", "word of mouth"]
value = [eve, ads, wom]
colors = ["blue", "red", "yellow"]

pyplot.pie(
    value,
    labels= labels,
    colors=colors
)
pyplot.axis('equal')
pyplot.show()