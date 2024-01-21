from pymongo import MongoClient
from dataclasses import dataclass
import pandas as pd

@dataclass
class mongodb :
    database : str
    collection : str
    
    def insert_one(self,doc):
        result = self.collection.insert_one(doc)
        print(f'insert id : {result.inserted_id}')        
    
    def insert_many(self,doc):
        result = self.collection.insert_many(doc)
        print(f'insert id : {result.inserted_ids}')

    # def close(self,client):
    #     client.close()

if __name__ == '__main__':

    database = 'novels'
    collection = "download"
    db = mongodb(database,collection)

    try :
        with MongoClient(f'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.1') as client :
            db = client.get_database(database)
            collection = db.get_collection(collection)

            # Example: Insert a document
            # document = {"key": "value"}
            # result = collection.insert_one(document)
            # print(f"Inserted document with ID: {result.inserted_id}")
            db.insert_one()
    except : 
        ...
    
    finally :
        client.close()