import asyncio
import datetime as dt
from discord.ext import commands, tasks
from discord import Embed
from random import choice
from helpers.quotes_helpers import get_random_quote, get_tag_list, get_random_quote_with_tag, get_random_anime_quote

class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.hourlyquote.start()

    # quotable_credits = 'API credits: https://github.com/lukePeavey/quotable'
    # animechan_credits = 'API credits: https://animechanapi.xyz/'

    starden_genchannel_id = 758361018233126936

    @tasks.loop(hours=1)
    async def hourlyquote(self):
        # isAnime = choice([True, False])
        isAnime = False
        starden_genchannel = self.bot.get_channel(Quotes.starden_genchannel_id)
        if isAnime:
            quote = get_random_anime_quote()
            embed = Embed(description=quote['content'], title=f'{quote["character"]} ({quote["anime"]})')
            embed.set_thumbnail(url='https://i.imgur.com/HeGEEbu.jpg')
        else:
            quote = get_random_quote()
            embed = Embed(description=quote['content'], title=quote['author'])
            embed.set_thumbnail(url='https://i.imgur.com/HeGEEbu.jpg')
        await starden_genchannel.send(embed=embed)

    @hourlyquote.before_loop
    async def before_hourlyquote(self):
        print('waiting for bot to be ready...')
        await self.bot.wait_until_ready()
        for _ in range(6*60*24):
            timenow = dt.datetime.now()
            # start loop at minute 0 of any hour, e.g., 12:00, 1:00, etc.
            if timenow.minute == 0:
                print('Starting loop.')
                break
            await asyncio.sleep(10)

    @commands.command(brief='display a random quote', aliases=['q'])
    async def quote(self, ctx, category : str = None):

        if category is None:
            quote = get_random_quote()
            embed = Embed(description=quote['content'], title=quote['author'])
            embed.set_thumbnail(url='https://i.imgur.com/HeGEEbu.jpg')
            # embed.set_footer(text=Quotes.quotable_credits)
            await ctx.send(embed=embed)
        else:
            category_list = get_tag_list()
            if category in category_list:
                if category == 'anime':
                    quote = get_random_anime_quote()
                    embed = Embed(description=quote['content'], title=f'{quote["character"]} ({quote["anime"]})')
                    embed.set_thumbnail(url='https://i.imgur.com/HeGEEbu.jpg')
                    # embed.set_footer(text=Quotes.animechan_credits)
                    await ctx.send(embed=embed)
                else:
                    quote = get_random_quote_with_tag(category)
                    embed = Embed(description=quote['content'], title=quote['author'])
                    embed.set_thumbnail(url='https://i.imgur.com/HeGEEbu.jpg')
                    # embed.set_footer(text=Quotes.quotable_credits)
                    await ctx.send(embed=embed)
            else:
                quote = None
                await ctx.send('No such category. Check list of categories with `*qcats`')


    @commands.command(brief='display a list of quote categories', aliases=['qc'])
    async def qcats(self, ctx):
        category_list = get_tag_list()
        content = 'Here\'s a list of quote categories:'
        for category in category_list:
            content += f'\n{category}'
        await ctx.send(f'```{content}```')

def setup(bot):
    bot.add_cog(Quotes(bot))
    print('Quotes cog successfully added.')