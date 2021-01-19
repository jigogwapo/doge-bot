from discord.ext import commands
from helpers.quotes_helpers import get_random_quote, get_tag_list, get_random_quote_with_tag

class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='display a random quote', aliases=['q'])
    async def quote(self, ctx, category : str = None):
        if category is None:
            quote = get_random_quote()
        else:
            category_list = get_tag_list()
            if category in category_list:
                quote = get_random_quote_with_tag(category)
            else:
                quote = None

        if quote is None:
            await ctx.send('No such category. Check list of categories with `*qcats`')
        else:
            await ctx.send(f'> *{quote["content"]}* - {quote["author"]}')

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