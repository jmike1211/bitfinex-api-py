import pymongo
import os
import sys

from config import Config

class useMongo():
    def __init__(self):
        self.client = pymongo.MongoClient(Config.config()["mongoConnect"])        
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

    def mongoupsertone(self, origintoken, changetoken, collectionName="account"):
        collection = self.db[collectionName]
        modify = collection.find_one(origintoken)
        print(modify)
        #modify[changename] = changetoken
        result = collection.update_one(origintoken, {'$set': changetoken},upsert=True)
        return result

#result = useMongo().mongodelone({"id" : "20170101"})
#print(result)
"""

result = useMongo().mongofindone({},"frrrate")
print(result)
if result == None:
    print("aaaaa")
else:
    print(result["frr"])

mongoResult = {}
mongoResult["frr"] = round(0.000325613,5)
mongoResult["hask"] = round(0.000842145613,5)
mongoResult["lprice"] = round(0.00017313,5)

result = useMongo().mongoupdateone({},mongoResult,"frrrate")
print(result)
print(result.matched_count, result.modified_count)
"""
