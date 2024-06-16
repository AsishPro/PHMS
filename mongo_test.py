from pymongo import MongoClient
import os

mongo_uri = os.environ.get('mongo_url')

client = MongoClient(mongo_uri)

db = client.phms
collection = db.users


document = {
    'name': 'asish',
    'email':'tempo@gmail.com',
    'password':"temppass"
}

result = collection.insert_one(document)
print(f'Inserted document with _id: {result.inserted_id}')