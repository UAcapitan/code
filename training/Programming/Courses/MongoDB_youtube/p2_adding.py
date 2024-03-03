
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://root:12345qwerty@cluster0.eybo9vm.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

try:
    client.admin.command('ping')
    
    db = client.test
    coll = db.new_users
    coll.insert_one({"_id":"test", "name":"Petya"})
except Exception as e:
    print(e)
