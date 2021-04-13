import pymongo

class Database(object):
    uri = "mongodb://127.0.0.1:27017" # this uri is called static variable as it is a class uri
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)# we have to mention database.uri as it is a class uri
        Database.DATABASE = client["fullstack"]

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
    #returns the element retrived by the cursor