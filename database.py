import pymongo


class Database(object):
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    # Tell Python that we're not going to use 'self',
    # as this method belongs to the class Database as a whole
    # and not an instance of a Database
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)