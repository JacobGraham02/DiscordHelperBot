import discord
import os
import frontend.main as frontend_main
from dotenv import load_dotenv

from backend.database.MongoDbDatabaseReader import MongoDbDatabaseReader
from backend.database.MongoDbDatabaseResultParser import MongoDbDatabaseResultParser
from frontend.main import PongGame
from frontend.main import PongApp

load_dotenv()

def main():
    frontend_main
    mongodb_database_reader = MongoDbDatabaseReader(os.getenv('MONGODB_CONNECTION_STRING'))
    mongodb_database_reader.connect_to_database()
    mongodb_database_reader.get_database_instance()
    mongodb_database_reader.get_collection_instance()
    # mongodb_database_reader.insert_document_into_collection()
    listOfDatabaseDocuments = mongodb_database_reader.get_documents_from_collection()
    mongodb_database_parser = MongoDbDatabaseResultParser(listOfDatabaseDocuments)
    
    
# client = discord.Client()

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
    
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')
        
# client.run(os.getenv('DISCORD_BOT_TOKEN'))

if __name__ == '__main__':
    main()