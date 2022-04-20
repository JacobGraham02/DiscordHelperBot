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
            
        dictionaryOfDatabaseDocumentsCounter = 0
        for document in listOfDatabaseDocuments:
            dictOfDatabaseDocuments[document['course_code']] = listOfDatabaseDocuments[dictionaryOfDatabaseDocumentsCounter]
            dictionaryOfDatabaseDocumentsCounter+=1
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
    