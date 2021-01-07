import discord, os
from dotenv import load_dotenv
from discord.ext.commands import Bot

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
async def ligo(ctx):
    await ctx.send('Maligo ka na uy!')

# insert the line below at the end of the file
# define <TOKEN> as your discord bot token
bot.run(TOKEN)