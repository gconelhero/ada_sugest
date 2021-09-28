cfrom pymongo import MongoClient
from datetime import datetime

class Database():
    
    def __init__(self, collection):
        try:    
            self.mongo_ins = MongoClient(host='192.168.0.16', 
            port=27017, 
            maxPoolSize=200
            )
            self.database_name = 'OpenAI'
            self.collection_name = collection
            self.connect = self.mongo_ins[self.database_name]
            self.database = self.connect[self.collection_name]
        
        except Exception as error:
            print("ERROR > ", str(error))
            raise error

    def insert(self, prompt, json_response):
        try:    
            insert = self.database.insert_one(
                        {"Date": datetime.now().strftime('%Y-%b-%d'), 
                        "Hour": datetime.now().strftime('%Hh%Mm%Ss'),
                        "Prompt": prompt,
                        "OpenAI": json_response}).inserted_id
            return insert

        except Exception as error:
            print("ERROR > ", str(error))
            raise error