import discord, asyncio
import datetime as dt
import random
from discord.ext import commands, tasks
from helpers.paginate import paginate
from helpers.birthday_helpers import save_birthday, get_birthdays, get_birthdays_on, get_birthdays_today
from helpers.todo_helpers import create_user
from models.User import User

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bday_emoji_list = ['<a:happybirthday:805884658046205972>',
        '<:linus_gun:761509258499981342>', '<a:yykawaii_Yay_confetti:788707701424783421>']

    @commands.command(brief='save your birthday')
    async def bday(self, ctx, *args):
        if len(args) != 2:
            await ctx.send('Format should be `*bday MM DD`, ex. `*bday 12 1`')
        else:
            data = list(args)
            for index, num in enumerate(args):
                try:
                    data[index] = int(num)
                except Exception as ex:
                    # print(ex)
                    # await ctx.send('Input must be integers.')
                    await ctx.send(ex)
                    break
            else:
                try:
                    if not User.objects(discord_id=ctx.author.id):
                        create_user(ctx.author.id)
                    save_birthday(ctx.author.id, *data)
                    await ctx.send('Birthday has been saved.')
                except:
                    await ctx.send('That doesn\'t seem like a valid date.')

    @commands.command(brief='display a list of birthdays')
    async def bdaylist(self, ctx):
        birthday_list = get_birthdays()
        content = 'Here\'s a list of birthdays:'
        for user in birthday_list:
            user_name = self.bot.get_user(user.discord_id).display_name
            bdaystring = f'{user.birthday.strftime("%B")} {user.birthday.day}'
            content += f'\n{bdaystring} - {user_name}'
        await ctx.send(f'```{content}```')

    @commands.command(brief='display users with birthdays on a given day')
    async def bdayon(self, ctx, *args):
        if len(args) != 2:
            await ctx.send('Format should be `*bdayon MM DD`, ex. `*bdayon 12 1`')
        else:
            data = list(args)
            for index, num in enumerate(args):
                try:
                    data[index] = int(num)
                except Exception as ex:
                    # print(ex)
                    # await ctx.send('Input must be integers.')
                    await ctx.send(ex)
                    break
            else:
                try:
                    emoji = random.choice(Info.bday_emoji_list)
                    if not User.objects(discord_id=ctx.author.id):
                        create_user(ctx.author.id)
                    users = get_birthdays_on(*data)
                    givendate = dt.date(year=2000, month=data[0], day=data[1])
                    bdaystring = f'{givendate.strftime("%B")} {givendate.day}'
                    if not users:
                        await ctx.send('Walang manglilibre sa {bdaystring}.')
                    else:
                        await ctx.send(emoji)
                        content = f'Eto yung mga manglilibre sa {bdaystring}:'
                        content += '```'
                        for user in users:
                            user_name = self.bot.get_user(user.discord_id).display_name
                            content += f'\n{user_name}'
                        await ctx.send(f'{content}```')
                except:
                    await ctx.send('That doesn\'t seem like a valid date.')

    @commands.command(brief='display users whose birthday is today')
    async def bdaynow(self, ctx):
        if not User.objects(discord_id=ctx.author.id):
            create_user(ctx.author.id)
        users = get_birthdays_today()
        if not users:
            await ctx.send('Walang manglilibre ngayon. :(')
        else:
            content = 'Happy birthday! Palibre naman!'
            for user in users:
                user_name = self.bot.get_user(user.discord_id).display_name
                content += f'\n{user_name}'
            await ctx.send(f'```{content}```')

    @tasks.loop(hours=24)
    async def birthdaygreeting(self):
        pass

    @birthdaygreeting.before_loop
    async def before_birthdaygreeting(self):
        await self.bot.wait_until_ready()
        for _ in range(6*60*24):
            if dt.datetime.now().hour == 0:
                print('Starting loop at exactly Midnight.')
                break
            await asyncio.sleep(10)

    @commands.command(brief='displays first 20 (for now) members of a role', aliases=['sa'])
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