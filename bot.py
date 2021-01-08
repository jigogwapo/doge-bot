import os, discord
from jeje_function import jejenizer
# from dotenv import load_dotenv
from discord.ext.commands import Bot
# from discord.utils import get

# load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

bot = Bot(command_prefix='*')

def no_everyone_here(text):
    return text.replace('@everyone', '[REDACTED]').replace('@here', '[REDACTED]')

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')

@bot.command(brief='for saying you\'re pogi')
async def pogi(ctx, *args):
    if len(args)==0:
        await ctx.send('Pogi talaga ni jigs!')
    else:
        text = no_everyone_here(args[0])
        await ctx.send(f'Pogi talaga ni {text}!')

@bot.command(brief='for saying you\'re ganda')
async def ganda(ctx, *args):
    if len(args)==0:
        await ctx.send('Ganda ka girl?')
    else:
        text = no_everyone_here(args[0])
        await ctx.send(f'Ganda naman ni {text}!')

@bot.command(brief='para sa mga @DI-NALILIGO')
async def ligo(ctx, *args):
    if len(args) == 0:
        await ctx.send('Maligo ka na uy!')
    else:
        text = no_everyone_here(args[0])
        await ctx.send(f'Maligo ka na nga {text}!')

@bot.command(brief=':kiss:')
async def kiss(ctx, *args):
    if len(args) == 0:
        await ctx.send('Pakiss nga!')
    else:
        text = no_everyone_here(args[0])
        await ctx.send(f'Pakiss nga {text}!')

@bot.command(brief='for saying you\'re chararat')
async def chararat(ctx, *args):
    if len(args) == 0:
        await ctx.send('ang chararat mo!')
    else:
        text = no_everyone_here(args[0])
        await ctx.send(f'ang chararat mo {text}!')

@bot.command(brief='you can ignore this')
async def fastpp(ctx):
    await ctx.send('https://streamable.com/pctmah')

@bot.command(brief='ex. *bonk umayos ka')
async def bonk(ctx, *args):
    if len(args) == 0:
        wordsurl = ''
    else:
        wordsurl='/'+'_'.join(args)
    await ctx.send(f'https://api.memegen.link/images/custom{wordsurl}.png?background=https://i.imgur.com/02w1SGO.jpg')

@bot.command(brief='ex. *jeje Hello guys!')
async def jeje(ctx, *args):
    if len(args) == 0:
        await ctx.send('waALha Kha Nh/-\mM@nN6 T!NyYPeE')
    else:
        input_text = ' '.join(args)
        jeje_text = jejenizer(input_text)
        await ctx.send(jeje_text)

@bot.command(brief='ex. *doge "top text" "bottom text"')
async def doge(ctx, *args):
    if len(args) == 0:
        await ctx.send('https://api.memegen.link/images/doge.png')
    elif len(args) >= 3:
        await ctx.send('too many phrases')
    elif len(args) == 1:
        text = args[0].replace(' ', '_')
        await ctx.send(f'https://api.memegen.link/images/doge/{text}.png')
    else:
        text1 = args[0].replace(' ', '_')
        text2 = args[1].replace(' ', '_')
        await ctx.send(f'https://api.memegen.link/images/doge/{text1}/{text2}.png')

@bot.command()
async def sinoang(ctx, *, role: discord.Role):
  await ctx.send(f'{role.members[0].name}')

bot.run(TOKEN)
