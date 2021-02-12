from discord.ext import commands
from helpers.jeje import jejenizer
from helpers.general_helpers import record_usage

def no_everyone_here(text):
    return text.replace('@everyone', '[REDACTED]').replace('@here', '[REDACTED]')
class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='for saying you\'re pogi')
    @commands.before_invoke(record_usage)
    async def pogi(self, ctx, *args):
        if len(args)==0:
            await ctx.send('Pogi talaga ni jigs!')
        else:
            text = no_everyone_here(args[0])
            await ctx.send(f'Pogi talaga ni {text}!')

    @commands.command(brief='for saying you\'re ganda')
    @commands.before_invoke(record_usage)
    async def ganda(self, ctx, *args):
        if len(args)==0:
            await ctx.send('Ganda ka girl?')
        else:
            text = no_everyone_here(args[0])
            await ctx.send(f'Ganda naman ni {text}!')

    @commands.command(brief='para sa mga @DI-NALILIGO')
    @commands.before_invoke(record_usage)
    async def ligo(self, ctx, *args):
        if len(args) == 0:
            await ctx.send('Maligo ka na uy!')
        else:
            text = no_everyone_here(args[0])
            await ctx.send(f'Maligo ka na nga {text}!')

    @commands.command(brief=':kiss:')
    @commands.before_invoke(record_usage)
    async def kiss(self, ctx, *args):
        if len(args) == 0:
            await ctx.send('Pakiss nga!')
        else:
            text = no_everyone_here(args[0])
            await ctx.send(f'Pakiss nga {text}!')

    @commands.command(brief='delete')
    @commands.before_invoke(record_usage)
    async def delete(self, ctx, *args):
        await ctx.send('My goodnessssss\nWe need to delete this server asap')

    @commands.command(brief='for saying you\'re chararat')
    @commands.before_invoke(record_usage)
    async def chararat(self, ctx, *args):
        if len(args) == 0:
            await ctx.send('ang chararat mo!')
        else:
            text = no_everyone_here(args[0])
            await ctx.send(f'ang chararat mo {text}!')

    @commands.command(brief='ex. *bonk umayos ka')
    @commands.before_invoke(record_usage)
    async def bonk(self, ctx, *, arg = ''):
        if arg == '':
            wordsurl = ''
        else:
            wordsurl= '/' + arg.replace(' ', '_').replace('-', '--')
        await ctx.send(f'https://api.memegen.link/images/custom{wordsurl}.png?background=https://i.imgur.com/02w1SGO.jpg')

    @commands.command(brief='ex. *bang umayos ka')
    @commands.before_invoke(record_usage)
    async def bang(self, ctx, *args):
        if len(args) == 0:
            wordsurl = ''
        else:
            wordsurl='/'+'_'.join(args)
        await ctx.send(f'https://api.memegen.link/images/custom{wordsurl}.png?background=https://i.imgur.com/mlJIOl5.jpg')

    @commands.command(brief='ex. *doge "top text" "bottom text"')
    @commands.before_invoke(record_usage)
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

    @commands.command(brief='ex. *jeje Hello guys!')
    @commands.before_invoke(record_usage)
    async def jeje(self, ctx, *args):
        if len(args) == 0:
            await ctx.send(jejenizer('Wala ka namang tinype!'))
        else:
            input_text = ' '.join(args)
            jeje_text = jejenizer(input_text)
            await ctx.send(jeje_text)

def setup(bot):
    bot.add_cog(Memes(bot))
    print('Memes cog successfully added.')