import discord, asyncio
import datetime as dt
import random
from discord.ext import commands, tasks
from helpers.reaction_helpers import paginate, add_delete_button
from helpers.birthday_helpers import save_birthday, get_birthdays, get_birthdays_on, get_birthdays_today
from helpers.todo_helpers import create_user
from helpers.general_helpers import record_usage
from models.User import User

def check_if_bday_channel(ctx):
    return ctx.channel.id == 806463388015132712

def get_bdaystring(month, day):
    givendate = dt.date(year=2000, month=month, day=day)
    bdaystring = f'{givendate.strftime("%B")} {givendate.day}'
    return bdaystring
class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.birthdaygreeting.start()

    bday_emoji_list = [
        '<a:happybirthday:805884658046205972>',
        '<:linus_gun:761509258499981342>',
        '<a:yykawaii_Yay_confetti:788707701424783421>',
        '<a:yypink_BouncyCake:803970227708362772>',
        '<a:yykawaii_baby_dance:788687662705934336>',
        '<a:zzNekoAtsume_jump:804348020992507924>'
        ]

    no_bday_emoji_list = [
        '<:peepo_sad:760424879978709012>',
        '<:starden_cat_criKet:760355767777361960>',
        '<:wtfpain:764528591618310154>',
        '<a:excuseme:791200676264017960>'
    ]

    starden_guild_id = 758361018233126932
    starden_bday_channel_id = 806463388015132712

    async def post_bday_card(self, channel):
        await channel.send(file=discord.File('static/starden_bday_card.png'))

    async def post_greeting(self):
        bday_channel = self.bot.get_channel(Info.starden_bday_channel_id)
        users = get_birthdays_today()
        if users:
            greeting='STARDENBURDENHARDENBART! It\'s {} burrthday{} today! Don\'t forget to greet them!'
            mention_strings = [f'<@{user.discord_id}>' for user in users]
            if len(users) >= 2:
                mentions = ', '.join(mention_strings[:-1]) + f' and {mention_strings[-1]}'
                plural='s'
            else:
                mentions = mention_strings[0]
                plural=''
            content = greeting.format(mentions,plural)
            await bday_channel.send(content)
            await Info.post_bday_card(self, channel=bday_channel)

    @commands.before_invoke(record_usage)
    @commands.command(brief='save your birthday')
    @commands.check(check_if_bday_channel)
    async def bday(self, ctx, *args):
        if len(args) != 2:
            await ctx.send('Format should be `*bday MM DD`, ex. `*bday 12 1`', delete_after=10)
        else:
            data = list(args)
            for index, num in enumerate(args):
                try:
                    data[index] = int(num)
                except Exception as ex:
                    await ctx.send(ex, delete_after=10)
                    break
            else:
                try:
                    if not User.objects(discord_id=ctx.author.id):
                        create_user(ctx.author.id)
                    save_birthday(ctx.author.id, *data)
                    emoji = random.choice(Info.bday_emoji_list)
                    await ctx.send(emoji, delete_after=10)
                    await ctx.send(f'Birthday ({get_bdaystring(*data)}) has been saved.', delete_after=10)
                except:
                    await ctx.send('That doesn\'t seem like a valid date.', delete_after=10)
        await ctx.message.delete(delay=5)

    @commands.before_invoke(record_usage)
    @commands.command(brief='display a list of birthdays')
    # @commands.has_any_role('Arbiter', 'Bot Meowster')
    async def bdaylist(self, ctx):
        birthday_list = get_birthdays()
        content = 'Here\'s a list of birthdays:'
        starden_guild = self.bot.get_guild(Info.starden_guild_id)
        for user in birthday_list:
            try:
                user_name = starden_guild.get_member(user.discord_id).display_name
                bdaystring = f'{user.birthday.strftime("%B")} {user.birthday.day}'
                content += f'\n{bdaystring} - {user_name}'
            except:
                pass
        message = await ctx.send(f'```{content}```')
        await add_delete_button(ctx, self.bot, message)

    @commands.before_invoke(record_usage)
    @commands.command(brief='display users with birthdays on a given day')
    @commands.has_any_role('Arbiter', 'Bot Meowster')
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
                    if not User.objects(discord_id=ctx.author.id):
                        create_user(ctx.author.id)
                    users = get_birthdays_on(*data)
                    givendate = dt.date(year=2000, month=data[0], day=data[1])
                    bdaystring = f'{givendate.strftime("%B")} {givendate.day}'
                    if not users:
                        emoji = random.choice(Info.no_bday_emoji_list)
                        await ctx.send(emoji)
                        await ctx.send(f'Walang manglilibre sa {bdaystring}.')
                    else:
                        emoji = random.choice(Info.bday_emoji_list)
                        await ctx.send(emoji)
                        content = f'Eto yung mga manglilibre sa {bdaystring}:'
                        content += '```'
                        for user in users:
                            user_name = self.bot.get_user(user.discord_id).display_name
                            content += f'\n{user_name}'
                        await ctx.send(f'{content}```')
                except:
                    await ctx.send('That doesn\'t seem like a valid date.')

    @commands.before_invoke(record_usage)
    @commands.command(brief='posts bday commands to #birthdays channel')
    @commands.has_any_role('Arbiter', 'Bot Meowster')
    async def bdayposthelp(self, ctx):
        bday_channel = self.bot.get_channel(Info.starden_bday_channel_id)
        content = '''To add birthday to database, use the command: `*bday MM DD`
        e.g. `*bday 4 20` (if your birthday is on April 20)
        '''
        await bday_channel.send(content)

    @tasks.loop(hours=24)
    async def birthdaygreeting(self):
        print('Running birthday loop instance.')
        await Info.post_greeting(self)

    @birthdaygreeting.before_loop
    async def before_birthdaygreeting(self):
        print('waiting for bot to be ready...')
        await self.bot.wait_until_ready()
        for _ in range(6*60*24):
            timenow = dt.datetime.now()
            if timenow.hour == 6 and timenow.minute == 0:
                print('Starting loop.')
                break
            await asyncio.sleep(10)

    @commands.before_invoke(record_usage)
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