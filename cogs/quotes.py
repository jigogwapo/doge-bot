from discord.ext import commands
from helpers.quotes_helpers import get_random_quote

class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='display a random quote')
    async def quote(self, ctx):
        quote = get_random_quote()
        await ctx.send(f'> *{quote["content"]}* - {quote["author"]}')

def setup(bot):
    bot.add_cog(Quotes(bot))
    print('Quotes cog successfully added.')