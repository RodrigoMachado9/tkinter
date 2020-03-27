from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db_trainning = client['db_tranning']
collection = db_trainning['working_jsons']


