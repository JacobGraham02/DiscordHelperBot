import discord
import os
import frontend.main as frontend_main
from dotenv import load_dotenv
from discord.ext import commands

from backend.classes import CommandManager
from backend.database.MongoDbDatabaseReader import MongoDbDatabaseReader
from backend.database.MongoDbDatabaseResultParser import MongoDbDatabaseResultParser

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_BOT_TOKEN_ID')
DISCORD_CHANNEL = os.getenv('DISCORD_CHANNEL_ID')
GUILD_TOKEN = os.getenv('DISCORD_GUILD_ID')

bot = commands.Bot(command_prefix='/')

def main():
    mongodb_database_reader = MongoDbDatabaseReader(os.getenv('MONGODB_CONNECTION_STRING'))
    mongodb_database_reader.connect_to_database()
    mongodb_database_reader.get_database_instance()
    mongodb_database_reader.get_collection_instance()
    mongodb_database_reader.insert_document_into_collection()
    dictOfDatabaseDocuments = mongodb_database_reader.get_dictionary_of_documents_from_collection()
    
    @bot.event
    async def on_ready():
        print('We have logged in as {0} to Discord'.format(bot.user.name))
        
    bot.run(DISCORD_TOKEN)
    
@bot.command(name='99')
async def nine_nine(ctx):
    response = "hello"
    await ctx.send(response)
    
if __name__ == '__main__':
    main()