import os, discord, asyncio
from jeje_function import jejenizer
import discord.ext.commands as commands
intents = discord.Intents.all()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

bot = commands.Bot(command_prefix='*', intents=intents)
client = discord.Client()

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

@bot.command(brief='ex. *bang umayos ka')
async def bang(ctx, *args):
    if len(args) == 0:
        wordsurl = ''
    else:
        wordsurl='/'+'_'.join(args)
    await ctx.send(f'https://api.memegen.link/images/custom{wordsurl}.png?background=https://i.imgur.com/mlJIOl5.jpg')

@bot.command(brief='ex. *jeje Hello guys!')
async def jeje(ctx, *args):
    if len(args) == 0:
        await ctx.send(jejenizer('Wala ka namang tinype!'))
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

@bot.command(brief='displays first 20 (for now) members of a role')
async def sinoang(ctx, *, role: discord.Role):
    pg_len = 20                     # items per page
    mem_len = len(role.members)     # total number of members
    # pg1_len = min(mem_len, pg_len)
    pages = mem_len // pg_len + 1    # total number of pages
    cur_page = 1                     # current page number

    def page_content(page_num):
        content = f'Eto yung mga {role.name} ({mem_len} total):\n\n'
        if page_num == 1:
            page_end = min(mem_len, pg_len)
        else:
            page_end = page_num*pg_len

        for i in role.members[(page_num-1)*pg_len:page_end]:
            content += f'{i.name}\n'
        content += f'\nPage {page_num} of {pages}'
        return f'```{content}```'

    message = await ctx.send(page_content(cur_page))

    await message.add_reaction('◀')
    await message.add_reaction('❌')
    await message.add_reaction('▶')

    def check_react(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['◀', '❌', '▶']

    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60, check=check_react)

            if str(reaction.emoji) == '◀' and cur_page > 1:
                cur_page -= 1
                await message.edit(content=page_content(cur_page))
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == '▶' and cur_page != pages:
                cur_page += 1
                await message.edit(content=page_content(cur_page))
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == '❌':
                await message.delete()

            else:
                await message.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            await message.delete()
            break



@sinoang.error
async def sinoang_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('WALA')

bot.run(TOKEN)
