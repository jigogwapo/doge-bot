import os, discord, asyncio
from jeje_function import jejenizer
from books import book_search, author_book_search
import discord.ext.commands as commands
intents = discord.Intents.all()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

bot = commands.Bot(command_prefix='*', intents=intents)
client = discord.Client()

starden_server_id = 758361018233126932
starden_anonchannel_id = 789854981981077514
starden_testchannel_id = 780701253280727040


def no_everyone_here(text):
    return text.replace('@everyone', '[REDACTED]').replace('@here', '[REDACTED]')

async def paginate(ctx, content_list, *, isEmbed=False):
    if isEmbed:
        message = await ctx.send(embed=content_list[0])
    else:
        message = await ctx.send(content=content_list[0])

    async def edit_message(message, data):
        if isEmbed:
            await message.edit(content=None, embed=data)
        else:
            await message.edit(embed=None, content=data)

    list_len = len(content_list)
    cur_page = 1
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
                await edit_message(message, content_list[cur_page-1])
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == '▶' and cur_page != list_len:
                cur_page += 1
                await edit_message(message, content_list[cur_page-1])
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == '❌':
                await message.delete()

            else:
                await message.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            await message.delete()
            break

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    starden_server = bot.get_guild(starden_server_id)
    if not message.guild: # for solo dms
        if message.content.startswith('*anon') and starden_server.get_member(message.author.id) is not None:
            starden_anonchannel = bot.get_channel(starden_anonchannel_id)
            anon_message = message.content[6:]
            await starden_anonchannel.send(f'**anon**: {anon_message}')
            await message.channel.send(f'anon message successfully sent. you can now delete your DM.')
    await bot.process_commands(message)

@bot.command(brief='search for a book')
async def book(ctx, *, book_name):
    book = book_search(book_name)
    if book is None:
        await ctx.send('No book found.')
    else:
        embed = discord.Embed(title=book['title'], url=book['url'], description=book['description'])
        embed.set_author(name=book['author'])
        embed.set_thumbnail(url=book['image'])
        await ctx.send(embed=embed)

@bot.command(brief='search for an author\'s books')
async def author(ctx, *, author_name):
    author_books_list = author_book_search(author_name)
    if author_books_list is None:
        await ctx.send(f'No book found by {author_name}.')
    else:
        # create list of embeds
        book_embeds_list = []
        for i in range(len(author_books_list)):
            book = author_books_list[i]
            embed = discord.Embed(title=f'{i+1}. {book["title"]}', url=book['url'], description=book['description'])
            embed.set_thumbnail(url=book['image'])
            book_embeds_list.append(embed)
        await ctx.send(f'Here are {author_name}\'s top 5 books:')
        await paginate(ctx, book_embeds_list, isEmbed=True)

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

@bot.command(brief='displays first 20 (for now) members of a role')
async def sinoang(ctx, *, role: discord.Role):
    pg_len = 20                     # items per page
    mem_len = len(role.members)     # total number of members
    # pg1_len = min(mem_len, pg_len)
    pages = mem_len // pg_len + 1    # total number of pages
    # build page_content_list
    page_content_list = []

    for page_num in range(1, pages+1):
        page_content = f'Eto yung mga {role.name}:\n'

        if page_num == 1:
            page_end = min(mem_len, pg_len)
        else:
            page_end = page_num*pg_len

        for member in role.members[(page_num-1)*pg_len:page_end]:
            page_content += f'{member.name}\n'

        page_content += f'Page {page_num} of {pages}'
        page_content_list.append(f'```{page_content}```')

    # runs paginate helper function to automatically create pages on discord
    await paginate(ctx, page_content_list)

@sinoang.error
async def sinoang_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('WALA')

bot.run(TOKEN)