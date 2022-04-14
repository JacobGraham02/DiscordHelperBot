from dotenv import load_dotenv
from pymongo import MongoClient
import pymongo
from datetime import datetime

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
        
    def get_dictionary_of_documents_from_collection(self):
        dictOfDatabaseDocuments = {}
        listOfDatabaseDocuments = []
        cursorOfDatabaseObjects = self.collection.find()
        
        for document in cursorOfDatabaseObjects:
            listOfDatabaseDocuments.append(document)
            
        i = 0
        for document in listOfDatabaseDocuments:
            dictOfDatabaseDocuments[document['course_code']] = listOfDatabaseDocuments[i]
            i+=1
            
        print(dictOfDatabaseDocuments)
        return dictOfDatabaseDocuments
            
    def insert_document_into_collection(self):
        test_post = {"course_code": "Test course code 2006",
                     "course_work_name": "Test course work name",
                     "course_work_due_date": "Test course work due date",
                     "course_work_input_date": datetime.today().strftime('%Y-%m-%d'),
                     "course_work_extra_information": "Test course work extra information"}
        self.posts.insert_one(test_post)
    
    def get_documents_from_collection_by_code(self):
        listOfDatabaseDocuments = []
        for document in self.collection.find({"author":"Mike"}):
            listOfDatabaseDocuments.append(document)
        return listOfDatabaseDocuments
    