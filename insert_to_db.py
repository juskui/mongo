import mongo_connection

client = mongo_connection.connect()

db = client["taskDB"]
coll = db["task_collection"]

data = [
    {"id": 1, "task": "siivous"},
    {"id": 2, "task": "putsaus"},
    {"id": 3, "task": "puunaus"},
]

coll.insert_many(data)
