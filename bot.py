import os, discord
from dotenv import load_dotenv
from discord.ext.commands import Bot
# from discord.utils import get

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

bot = Bot(command_prefix='$') # or whatever prefix you choose(!,%,?)

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')

# @bot.event
# async def on_message(message):
# 	if message.content == 'test':
# 		await message.channel.send('Testing 1 2 3!')

@bot.command()
async def pogi(ctx, *args):
    if len(args)==0:
        await ctx.send('Pogi talaga ni jigs!')
    else:
        await ctx.send(f'Pogi talaga ni {args[0]}!')

@bot.command()
async def ligo(ctx, *args):
    if len(args) == 0:
        await ctx.send('Maligo ka na uy!')
    else:
        await ctx.send(f'Maligo ka na nga {args[0]}!')

@bot.command()
async def kiss(ctx, *args):
    if len(args) == 0:
        await ctx.send('Pakiss nga!')
    else:
        await ctx.send(f'Pakiss nga {args[0]}!')

@bot.command()
async def chararat(ctx, *args):
    if len(args) == 0:
        await ctx.send('ang chararat mo!')
    else:
        await ctx.send(f'ang chararat mo {args[0]}!')

@bot.command()
async def listmembers(ctx, *, role: discord.Role):
    # if len(args)==0:
    #     await ctx.send('You\'re supposed to supply a role!')
    print(role.name)
    print(type(role))
    print(role.members)
    # await ctx.send(f'Here are the members of {role.name}:')
    # for user in role.members[0]:
    #     await ctx.send(user.name)

@bot.command()
async def roles(ctx):
    for i in ctx.guild.roles[:10]:
        await ctx.send(i.name)

# insert the line below at the end of the file
# define <TOKEN> as your discord bot token
bot.run(TOKEN)