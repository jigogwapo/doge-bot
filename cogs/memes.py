from discord.ext import commands
from discord import Embed
from helpers.jeje import jejenizer
from helpers.general_helpers import record_usage, get_random_question
from helpers.dadjoke_helpers import get_random_dadjoke

def no_everyone_here(text):
    return text.replace('@everyone', '[REDACTED]').replace('@here', '[REDACTED]')
class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.before_invoke(record_usage)
    @commands.command(brief='for saying you\'re pogi')
    async def pogi(self, ctx, *args):
        if len(args)==0:
            await ctx.send('Pogi talaga ni jigs!')
        else:
            text = no_everyone_here(args[0])
            await ctx.send(f'Pogi talaga ni {text}!')

    @commands.before_invoke(record_usage)
    @commands.command(brief='for saying you\'re ganda')
    async def ganda(self, ctx, *args):
        if len(args)==0:
            await ctx.send('Ganda ka girl?')
        else:
            text = no_everyone_here(args[0])
            await ctx.send(f'Ganda naman ni {text}!')

    @commands.before_invoke(record_usage)
    @commands.command(brief='para sa mga @DI-NALILIGO')
    async def ligo(self, ctx, *args):
        if len(args) == 0:
            await ctx.send('Maligo ka na uy!')
        else:
            text = no_everyone_here(args[0])
            await ctx.send(f'Maligo ka na nga {text}!')

    @commands.before_invoke(record_usage)
    @commands.command(brief=':kiss:')
    async def kiss(self, ctx, *args):
        if len(args) == 0:
            await ctx.send('Pakiss nga!')
        else:
            text = no_everyone_here(args[0])
            await ctx.send(f'Pakiss nga {text}!')

    @commands.before_invoke(record_usage)
    @commands.command(brief='delete')
    async def delete(self, ctx, *args):
        await ctx.send('My goodnessssss\nWe need to delete this server asap')

    @commands.before_invoke(record_usage)
    @commands.command(brief='anything for u bb')
    async def wisn(self, ctx, *args):
        await ctx.send('*anything 4 u bb*')

    @commands.before_invoke(record_usage)
    @commands.command(brief='for saying you\'re chararat')
    async def chararat(self, ctx, *args):
        if len(args) == 0:
            await ctx.send('ang chararat mo!')
        else:
            text = no_everyone_here(args[0])
            await ctx.send(f'ang chararat mo {text}!')

    @commands.before_invoke(record_usage)
    @commands.command(brief='ex. *bonk umayos ka')
    async def bonk(self, ctx, *, arg = ''):
        if arg == '':
            wordsurl = ''
        else:
            wordsurl= '/' + arg.replace(' ', '_').replace('-', '--')
        await ctx.send(f'https://api.memegen.link/images/custom{wordsurl}.png?background=https://i.imgur.com/02w1SGO.jpg')

    @commands.before_invoke(record_usage)
    @commands.command(brief='ex. *bang umayos ka')
    async def bang(self, ctx, *args):
        if len(args) == 0:
            wordsurl = ''
        else:
            wordsurl='/'+'_'.join(args)
        await ctx.send(f'https://api.memegen.link/images/custom{wordsurl}.png?background=https://i.imgur.com/mlJIOl5.jpg')

    @commands.before_invoke(record_usage)
    @commands.command(brief='ex. *doge "top text" "bottom text"')
    async def doge(self, ctx, *args):
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

    @commands.before_invoke(record_usage)
    @commands.command(brief='ex. *jeje Hello guys!')
    async def jeje(self, ctx, *args):
        if len(args) == 0:
            await ctx.send(jejenizer('Wala ka namang tinype!'))
        else:
            input_text = ' '.join(args)
            jeje_text = jejenizer(input_text)
            await ctx.send(jeje_text)

    @commands.before_invoke(record_usage)
    @commands.command(brief='get a random dad joke')
    async def dadjoke(self, ctx, *args):
        dadjoke = get_random_dadjoke()
        embed = Embed(description=dadjoke)
        embed.set_thumbnail(url='https://i.imgur.com/HeGEEbu.jpg')
        await ctx.send(embed=embed)

    @commands.before_invoke(record_usage)
    @commands.command(brief='get a random question')
    async def smalltalk(self, ctx, *args):
        question = get_random_question()
        embed = Embed(description=question)
        embed.set_thumbnail(url='https://i.imgur.com/HeGEEbu.jpg')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Memes(bot))
    print('Memes cog successfully added.')