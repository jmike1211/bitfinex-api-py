import pymongo
import os
import sys


class useMongo():
    def __init__(self):
        self.client = pymongo.MongoClient("")        
        self.db = self.client['bfxtest']

    def mongofindone(self, token={}, collectionName="account"):
        collection = self.db[collectionName]
        result = collection.find_one(token)
        return result

    def mongofindall(self, token, collectionName="account"):
        collection = self.db[collectionName]
        result = collection.find(token)
        return result

    def mongoinsertone(self, token, collectionName="account"):
        collection = self.db[collectionName]
        result = collection.insert_one(token)
        return result

    def mongodeleteone(self, token, collectionName="account"):
        collection = self.db[collectionName]
        result = collection.delete_one(token)
        return result

    def mongoupdateone(self, origintoken, changetoken, collectionName="account"):
        collection = self.db[collectionName]
        modify = collection.find_one(origintoken)
        print(modify)
        #modify[changename] = changetoken
        result = collection.update_one(origintoken, {'$set': changetoken})
        return result

