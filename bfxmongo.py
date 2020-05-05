import pymongo


class useMongo():
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv:<client>")        
        self.db = self.client['bfxtest']
        self.collection = self.db['account']

    def mongofindone(self, token):
        result = self.collection.find_one(token)
        return result

    def mongofind(self, token):
        result = self.collection.find(token)
        return result

    def mongoinsert(self, token):
        result = self.collection.insert(token)
        return result

    def mongodelone(self, token):
        result = self.collection.delete_one(token)
        return result


"""
result = useMongo().mongodelone({"id" : "20170101"})
print(result)

student = {
    'id': '20110101',
    'name': 'bike',
    'age': 23,
    'gender': 'male'
}

#useMongo().mongoinsert(student)

result = useMongo().mongofindone({"age" :{'$gt': 20}})
print(result)
if result == None:
    print("aaaaa")
else:
    print(result["gender"])


results = useMongo().mongofind({"age" :{'$gt': 20}})
print(results)
for i in results:
    print(i)
"""
