import os, discord
import discord.ext.commands as commands
from mongoengine import connect
from helpers.custom_text_helpers import get_commands
intents = discord.Intents.all()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
mongodb_uri = os.getenv('MONGODB_URI')

connect('starden', host=mongodb_uri)
print('Connected to database.')

bot = commands.Bot(command_prefix='*', activity=discord.Game(name='MONSTER HUNTER RISE'), intents=intents)

bot.load_extension('cogs.memes')
bot.load_extension('cogs.books')
bot.load_extension('cogs.info')
bot.load_extension('cogs.admin')
bot.load_extension('cogs.quotes')
bot.load_extension('cogs.todo')
bot.load_extension('cogs.anime')
bot.load_extension('cogs.customtext')
# bot.load_extension('cogs.wordle')

custom_command_list = get_commands()

def foo_factory(command):
    @commands.command(name=command.command_text)
    async def foo(ctx):
        await ctx.send(command.custom_text)
    return foo

for command in custom_command_list:
    bot.add_command(foo_factory(command))

async def is_in_botcommands(ctx):
    return ctx.channel.id == 758547575438704640

class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.blurple(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

custom_help = MyHelpCommand()
custom_help.add_check(is_in_botcommands)

bot.help_command = custom_help

bot.run(TOKEN)