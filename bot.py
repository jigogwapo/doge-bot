import os, discord
import discord.ext.commands as commands
intents = discord.Intents.all()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

bot = commands.Bot(command_prefix='*', intents=intents)

bot.load_extension('cogs.memes')
bot.load_extension('cogs.books')
bot.load_extension('cogs.info')
bot.load_extension('cogs.admin')
bot.load_extension('cogs.quotes')
bot.load_extension('cogs.todo')

bot.run(TOKEN)