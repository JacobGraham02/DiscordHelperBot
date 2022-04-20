import discord
import os
import frontend.main as frontend_main
from pprint import pprint
from dotenv import load_dotenv
from discord.ext import commands

from backend.classes.CommandManager import CommandManager 
from backend.database.MongoDbDatabaseReader import MongoDbDatabaseReader

bot = commands.Bot(command_prefix='/')

def main():
    dictionaryOfDatabaseDocuments = {}
    load_dotenv()
    
    MONGODB_CONNECTION_STRING = os.getenv('MONGODB_CONNECTION_STRING')
    DISCORD_TOKEN = os.getenv('DISCORD_BOT_TOKEN_ID')
    DISCORD_CHANNEL = os.getenv('DISCORD_CHANNEL_ID')
    GUILD_TOKEN = os.getenv('DISCORD_GUILD_ID')
    
    mongodb_database_reader = MongoDbDatabaseReader(MONGODB_CONNECTION_STRING)
    mongodb_database_reader.connect_to_database()
    mongodb_database_reader.get_database_instance()
    mongodb_database_reader.get_collection_instance()
    
    dictionaryOfDatabaseDocuments = mongodb_database_reader.get_dictionary_of_documents_from_collection()
    
    command_manager = CommandManager(dictionaryOfDatabaseDocuments)
    dictionaryOfDatabaseDocuments = command_manager.discord_commands
    # mongodb_database_reader.insert_document_into_collection()

    @bot.event
    async def on_ready():
        print('We have logged in as {0} to Discord'.format(bot.user.name))
        
    @bot.command()
    async def ninenine(ctx):
        response = "hello"
        await ctx.send(response)
            
    @bot.command()
    async def schoolwork(ctx):
        dictionaryOfDatabaseDocuments = mongodb_database_reader.get_dictionary_of_documents_from_collection()
        await ctx.send(dictionaryOfDatabaseDocuments)
        
            
    bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()