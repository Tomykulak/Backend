from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
from bson import ObjectId


# docker-compose build
# docker-compose up
# docker-compose down

# after loading docker, start mongoDB.py script to load data into database

app = FastAPI()

# Function to convert MongoDB documents to dictionaries
def mongo_to_dict(data):
    for document in data:
        document['_id'] = str(document['_id'])  # Convert ObjectId to string
        yield document

# Function to connect to MongoDB and retrieve data
def get_mongo_data():
    client = MongoClient("mongodb://mongodb:27017/")  # Connect to the MongoDB container
    db = client["mydatabase"]
    collection = db["mycollection"]
    data = list(collection.find())
    client.close()
    return list(mongo_to_dict(data))

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/test")
def read_test():
    return {"message": "Test!"}

@app.get("/mongo")
def read_mongodb_data():
    # Retrieve data from MongoDB using the imported function
    mongo_data = get_mongo_data()
    
    if mongo_data:
        try:
           return mongo_data
        except Exception as e:
            return {"message": "Error while serializing data", "error": str(e)}
    else:
        return {"message": "No data found in MongoDB"}

