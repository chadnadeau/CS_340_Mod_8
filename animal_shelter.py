from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username='aacuser', password='hockey4', host='nv-desktop-services.apporto.com', port=32418, db='AAC', col='animals'):
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, host, port))
        self.database = self.client[db]
        self.collection = self.database[col]

    def create(self, data):
        """Inserts a document into the specified MongoDB database and collection."""
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            print("Nothing to save because data parameter is empty")
            return False

    def read(self, filter_query=None):
        """Queries for documents from the specified MongoDB database and collection."""
        try:
            if filter_query is None:
                result = self.collection.find()
            else:
                result = self.collection.find(filter_query)
            return list(result)
        except Exception as e:
            print(f"An error occurred: {e}")
            return []


    def update(self, query, update_data):
        """Updates document(s) from a specified MongoDB database and specified collection."""
        try:
            result = self.collection.update_many(query, {'$set': update_data})
            return result.modified_count
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0

    def delete(self, query):
        """Removes document(s) from a specified MongoDB database and specified collection."""
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0


