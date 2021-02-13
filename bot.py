import os, discord
import discord.ext.commands as commands
from mongoengine import connect
intents = discord.Intents.all()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
mongodb_uri = os.getenv('MONGODB_URI')

connect('starden', host=mongodb_uri)
print('Connected to database.')

bot = commands.Bot(command_prefix='*', intents=intents)

bot.load_extension('cogs.memes')
bot.load_extension('cogs.books')
bot.load_extension('cogs.info')
bot.load_extension('cogs.admin')
bot.load_extension('cogs.quotes')
bot.load_extension('cogs.todo')
bot.load_extension('cogs.anime')

bot.run(TOKEN)