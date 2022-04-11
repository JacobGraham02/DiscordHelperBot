from gc import collect
from json import load
from dotenv import load_dotenv
from pymongo import MongoClient
import pymongo 
import pprint

load_dotenv

class MongoDbDatabaseReader:
    
    def __init__(self, database_connection_string, database_name = 'DiscordBot', collection_name = 'Work'):
        self.database_connection_string = database_connection_string
        self.database_name = database_name
        self.collection_name = collection_name
        
    # @database_type.setter
    # def database_type(self, value):
    #     if self.database_type == value:
    #         self.database_type = value
            
    # @property
    # def database_type(self):
    #     return self.database_type
    
    # def connect_to_database(self):
    #     self.client = MongoClient(self.database_connection_string)
    #     self.databaseConfig = self.client.config
        
    # def get_database_names(self):
    #     return self.client.list_database_names()
        
    # def get_collection_data(self):
    #     self.collection_instance = self.client[self.collection_name]
        
    #     cursor = self.collection_instance.find({})
    def connect_to_database(self):
        self.client = MongoClient(self.database_connection_string)
        self.database_config = self.client.config
        
    def get_database_instance(self):
        self.database = self.client[f'{self.database_name}']
        
    def get_collection_instance(self):
        self.collection = self.database[f'{self.collection_name}']
        self.posts = self.collection
        
    def get_documents_from_collection(self):
        listOfDatabaseDocuments = []
        for document in self.collection.find():
            listOfDatabaseDocuments.append(document)
        return listOfDatabaseDocuments
            
    def insert_document_into_collection(self):
        test_post = {"author": "Jack",
                     "text": "Test text",
                     "tags": ["MongoDb", "Python", "PyMongo"]}
        self.posts.insert_one(test_post)
    
    