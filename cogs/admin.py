from discord.ext import commands
import discord
from discord.utils import get
import random
from mongoengine.errors import DoesNotExist
from models.User import User
from helpers.todo_helpers import create_user
from helpers.general_helpers import record_usage
import asyncio
import datetime as dt

def get_anon_name(discord_id):
    user = User.objects(discord_id=discord_id).get()
    return user.anon_name

def add_anon_name(discord_id, anon_name):
    user = User.objects(discord_id=discord_id).get()
    anon_set_time = dt.datetime.now()
    user.anon_name = anon_name
    user.anon_set_time = anon_set_time
    user.save()

anonhelpstring = """DM these commands to <@796320516583063553> for posting anonymous messages on <#789854981981077514>:
>>> `*anon <msg>` - post an anonymous message as **anon**
`*sikret <msg>` - post a sikret message with a **sikretname**
`*setname <sikretname>` - set a **sikretname**"""
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc_delete_time = 1200
        self.setname_cooldown_minutes = 5

    starden_server_id = 758361018233126932
    starden_anonchannel_id = 789854981981077514
    starden_testchannel_id = 780701253280727040
    starden_voicechatchannel_id = 798943215008088155
    starden_genchannel_id = 758361018233126936
    starden_lobbychannel_id = 809668669226352691


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot connected as {self.bot.user}')
        await self.bot.change_presence(activity=discord.Activity(name="Valheim", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", type=discord.ActivityType.streaming, state="Running from Titan"))

    @commands.Cog.listener()
    async def on_message(self, message):
        starden_server = self.bot.get_guild(Admin.starden_server_id)
        if not message.guild: # for solo dms
            if starden_server.get_member(message.author.id) is not None:
                if message.content.startswith('*sikret'):
                    author_id = message.author.id

                    if not User.objects(discord_id=author_id):
                        create_user(author_id)

                    if not User.objects(discord_id=author_id, anon_name__exists=True):
                        await message.channel.send('<:dogehuh:810023920178561024>')
                        await message.channel.send('Set your anon name first using the `*setname` command.')
                    else:
                        anon_name = get_anon_name(author_id)
                        starden_anonchannel = self.bot.get_channel(Admin.starden_anonchannel_id)
                        purrfect_message = message.content[8:]
                        await starden_anonchannel.send(f'**{anon_name}**: {purrfect_message}')
                        await message.channel.send('<a:doge:788688516707385395>')
                        await message.channel.send('message sent meowster!')

                elif message.content.startswith('*anon'):
                    starden_anonchannel = self.bot.get_channel(Admin.starden_anonchannel_id)
                    anon_message = message.content[6:]
                    await starden_anonchannel.send(f'**anon**: {anon_message}')
                    await message.channel.send('<a:doge:788688516707385395>')
                    await message.channel.send('meowssage sent meowster!')


                elif message.content.startswith('*setname'):
                    author_id = message.author.id
                    anon_name = message.content[9:]
                    if not User.objects(discord_id=author_id):
                        create_user(author_id)
                    if len(anon_name) > 20:
                        await message.channel.send('Anon names cannot be longer than 20 characters.')
                    else:
                        try:
                            User.objects(anon_name=anon_name).get()
                            await message.channel.send('Your anon name is already taken. Kagaya ni crush.')
                        except DoesNotExist:
                            author_user = User.objects(discord_id=author_id).get()
                            try:
                                timediff = dt.datetime.now() - author_user.anon_set_time
                                cooldown = dt.timedelta(minutes=self.setname_cooldown_minutes)
                                if timediff > cooldown:
                                    add_anon_name(author_id, anon_name)
                                    await message.channel.send(f'Anon name set to **{anon_name}**')
                                else:
                                    timeleft = cooldown - timediff
                                    num_minutes = timeleft // dt.timedelta(minutes=1)
                                    num_seconds = (timeleft % dt.timedelta(minutes=1)).seconds
                                    await message.channel.send(f'Please wait {num_minutes} minutes and {num_seconds} seconds before setting a new anon name.')
                            except Exception as ex:
                                print(ex)
                                add_anon_name(author_id, anon_name)
                                await message.channel.send(f'Anon name set to **{anon_name}**')



                elif not message.author.bot:
                    user_name = message.author.name
                    await message.channel.send(f'MUCH WOW {user_name.upper()}. TALK ME AT STARDENBURDENHARDENBART.')

            else:
                await message.channel.send('...')

        if message.channel.id == Admin.starden_voicechatchannel_id:
            await asyncio.sleep(self.vc_delete_time)
            try:
                await message.delete()
            except:
                pass

        if message.reference is not None:
            author_roles = [role.name for role in message.author.roles]
            if message.reference.resolved.author.id == self.bot.user.id and "Green Teamer" in author_roles:
                if message.content.upper().startswith(('DELETE', 'SHUT UP', 'SILENCE', 'TAHIMIK', 'TUMAHIMIK', 'HIPOS')):
                    await message.add_reaction('👍')
                    await message.channel.send('YES BOT MEOWSTER', delete_after=5)
                    await message.reference.resolved.delete()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == Admin.starden_server_id:
            starden_genchannel = self.bot.get_channel(Admin.starden_genchannel_id)
            tarodancers = [
                '<a:doge:788688516707385395>',
                '<a:ztarden_TaroDanceSam:800943071545655346>',
                '<a:ztarden_TaroDanceCarrie:800952631165059122>',
                '<a:ztarden_TaroDanceErn:800954713113493514>'
                '<a:ztarden_TaroDancePrei:800947555210756136>',
                '<a:ztarden_TaroDanceManny:800947552458768425>',
                '<a:ztarden_JujuTaroDance:801241457474142228>'
                '<a:ztarden_TaroDanceKing:801239042012086283>',
                '<a:ztarden_TaroDanceGold:800950085344952352>',
                '<a:ztarden_TaroDanceGeros:801239041625686037>',
                '<a:ztarden_TaroDanceElder:801239041701052426>',
                '<a:doge_dance:788688533451178004>'
            ]
            await starden_genchannel.send(''.join(tarodancers))
            await starden_genchannel.send(f'Welcome new ket {member.mention} to STARDENBURDENHARDENBART! I\'m Doge-bot. You can check out my commands by typing `*help`.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == Admin.starden_server_id:
            starden_genchannel = self.bot.get_channel(Admin.starden_genchannel_id)
            sad_emotes = [
                '<:peepo_sad:760424879978709012>',
                '<:ztarden_cat_itsoKet:760341632381485057>',
                '<:ztarden_cat_surprizeKet:761723164702933013>',
                '<:wtfpain:764528591618310154>',
                '<a:pepe_cri:788706202108428323>',
                '<a:kawaii_UmaruChanCrying:788688980899004446>'
             ]
            sad_quotes = [
                 'Huhu iniwan na tayo ni **{mem_name}**. Pls com bak.',
                 'Tch! **{mem_name}** just left the server.',
                 'Bat mo kami iniwan, **{mem_name}**?',
                 'Iniwan tayo ni **{mem_name}** kagaya nung pagiwan sayo ng ex mo.'
             ]
            await starden_genchannel.send(random.choice(sad_emotes))
            await starden_genchannel.send(random.choice(sad_quotes).format(mem_name=member.display_name))

    @commands.before_invoke(record_usage)
    @commands.command(brief='mod command to change vc auto-delete time', aliases=['dt'])
    @commands.has_any_role('Arbiter', 'Bot Meowster', 'Gatekeeper')
    async def deltime(self, ctx, timeout: int = None):
        if timeout is None:
            await ctx.send(f'Current auto-delete time is {self.vc_delete_time} seconds.')
        else:
            self.vc_delete_time = timeout
            await ctx.send(f'Changed auto-delete time to {self.vc_delete_time} seconds.')

    @commands.before_invoke(record_usage)
    @commands.command(brief='mod command to change set name cooldown')
    @commands.has_any_role('Arbiter', 'Bot Meowster', 'Gatekeeper')
    async def namecd(self, ctx, timeout: int = None):
        if timeout is None:
            await ctx.send(f'Current cooldown time is {self.setname_cooldown_minutes} minutes.')
        else:
            self.setname_cooldown_minutes = timeout
            await ctx.send(f'Changed cooldown time to {self.setname_cooldown_minutes} minutes.')

    @deltime.error
    async def deltime_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Not a valid integer.')

    @commands.command(brief='post help for anon message commands')
    async def anonhelp(self, ctx):
        await ctx.send(anonhelpstring)

def setup(bot):
    bot.add_cog(Admin(bot))
    print('Admin cog successfully added.')