from pymongo import MongoClient

# Připojení k MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Výběr databáze
db = client["mydatabase"]

# Vytvoření kolekce
collection = db["mycollection"]

# Vložení dokumentu
people_to_insert = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
    {"name": "Eve", "age": 28},
    {"name": "Charlie", "age": 42},
    {"name": "Grace", "age": 22},
    {"name": "David", "age": 31},
    {"name": "Fiona", "age": 29},
    {"name": "Helen", "age": 37},
    {"name": "Isaac", "age": 26},
    {"name": "Linda", "age": 45}
]

# Insert each person into the collection
for person in people_to_insert:
    collection.insert_one(person)
    print(person)




# Define the aggregation pipeline to remove duplicates based on the "name" field
pipeline = [
    {"$group": {"_id": "$name", "unique_ids": {"$addToSet": "$_id"}, "count": {"$sum": 1}}},
    {"$match": {"count": {"$gt": 1}}}
]

# Execute the aggregation pipeline to identify duplicates
duplicates = list(collection.aggregate(pipeline))

# Iterate through the duplicates and remove them
for duplicate in duplicates:
    duplicate_name = duplicate['_id']
    duplicate_ids = duplicate['unique_ids'][1:]  # Skip the first ID (keep one)
    collection.delete_many({"_id": {"$in": duplicate_ids}})
    print(f"Duplicates for '{duplicate_name}' removed.")

print("Database cleaned of duplicates.")
