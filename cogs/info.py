import discord
from discord.ext import commands
from helpers.paginate import paginate

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='displays first 20 (for now) members of a role')
    async def sinoang(self, ctx, *, role: discord.Role):
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
        await paginate(ctx, self.bot, page_content_list)

    @sinoang.error
    async def sinoang_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('WALA')

def setup(bot):
    bot.add_cog(Info(bot))
    print('Info cog successfully added.')