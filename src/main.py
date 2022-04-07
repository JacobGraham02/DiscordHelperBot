import discord
import os
from dotenv import load_dotenv

from database.MongoDbDatabaseManager import MongoDbDatabaseManager

load_dotenv()

mongodb_database_manager = MongoDbDatabaseManager(os.getenv('MONGODB_CONNECTION_STRING'))
mongodb_database_manager.connect_to_database()
mongodb_database_manager.get_database_instance()
mongodb_database_manager.get_collection_instance()
mongodb_database_manager.get_documents_from_collection()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
client.run(os.getenv('DISCORD_BOT_TOKEN'))