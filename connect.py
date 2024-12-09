from pymongo import MongoClient


class BookstoreDB:
    def __init__(self, connection_string='mongodb://localhost:27017/'):
        self.client = MongoClient(connection_string)
        self.db = self.client['bookstore']

    def list_databases(self):
        return self.client.list_database_names()

    def get_book_collection(self, collection_name='Book'):
        return self.db[collection_name]

    def upsert_collection(self, collection_name, data):
        collection = self.db[collection_name]
        collection.insert_one(data)

    def close_connection(self):
        self.client.close()
