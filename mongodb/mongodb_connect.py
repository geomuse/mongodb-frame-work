from pymongo import MongoClient
from dataclasses import dataclass
import pandas as pd

@dataclass
class mongodb :
    database : str
    collection : str
    
    def connect(self) -> pd.DataFrame:
        client = MongoClient(f'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.1')
        db = client[self.database]
        self.collection = db[self.collection]
        # print(self.collection)
        return client

    def insert_one(self,doc):
        result = self.collection.insert_one(doc)
        print(f'insert id : {result.inserted_id}')
    
    def insert_many(self,doc):
        result = self.collection.insert_many(doc)
        print(f'insert id : {result.inserted_ids}')

    def filter(self,formula):
        """
        formula := "age more than 30" 
        """
        return self.collection().show(formula)

    def close(self,client):
        client.close()

    """
    资料库基本指令

    1. 可写 write : filter , delete , insert
    2. 可读 read : connect
    3. 可执行 exe : connect

    filter 是大方向.
    """

    """
    ...
    """

if __name__ == '__main__':

    db = mongodb(database='novels',collection='download')
    client = db.connect()
    db.close(client)