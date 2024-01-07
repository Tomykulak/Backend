from pymongo import MongoClient

# Připojení k MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Výběr databáze
db = client["mydatabase"]

# Vytvoření kolekce
collection = db["mycollection"]

# Vložení dokumentu
data = {"name": "John", "age": 30}
collection.insert_one(data)

# Dotaz na data
result = collection.find({"name": "John"})
for document in result:
    print(document)
