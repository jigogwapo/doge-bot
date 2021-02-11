from discord.ext import commands
from discord.utils import get
from mongoengine.errors import DoesNotExist
from models.User import User
from helpers.todo_helpers import create_user
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

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc_delete_time = 1200

    starden_server_id = 758361018233126932
    starden_anonchannel_id = 789854981981077514
    starden_testchannel_id = 780701253280727040
    starden_voicechatchannel_id = 798943215008088155
    starden_genchannel_id = 758361018233126936
    starden_lobbychannel_id = 807375880283619358

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot connected as {self.bot.user}')

    @commands.Cog.listener()
    async def on_message(self, message):
        starden_server = self.bot.get_guild(Admin.starden_server_id)
        if not message.guild: # for solo dms
            if starden_server.get_member(message.author.id) is not None:

                if message.content.startswith('*anon'):
                    starden_anonchannel = self.bot.get_channel(Admin.starden_anonchannel_id)
                    anon_message = message.content[6:]
                    await starden_anonchannel.send(f'**anon**: {anon_message}')
                    await message.channel.send(f'anon message successfully sent. you can now delete your DM.')

                elif message.content.startswith('*purrfect'):
                    author_id = message.author.id

                    if not User.objects(discord_id=author_id):
                        create_user(author_id)

                    if not User.objects(discord_id=author_id, anon_name__exists=True):
                        await message.channel.send('Set your anon name first using the `*setname` command.')
                    else:
                        anon_name = get_anon_name(author_id)
                        starden_lobbychannel = self.bot.get_channel(Admin.starden_lobbychannel_id)
                        purrfect_message = message.content[10:]
                        await starden_lobbychannel.send(f'**{anon_name}**: {purrfect_message}')
                        await message.channel.send('<a:zzNekoAtsume_jump:804348020992507924>')
                        await message.channel.send('meowssage sent! purrfect!')

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
                                if timediff > dt.timedelta(minutes=5):
                                    add_anon_name(author_id, anon_name)
                                    await message.channel.send(f'Anon name set to **{anon_name}**')
                                else:
                                    num_minutes = timediff // dt.timedelta(minutes=1)
                                    num_seconds = (timediff % dt.timedelta(minutes=1)).seconds
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

    @commands.command(brief='mod command to change vc auto-delete time', aliases=['dt'])
    @commands.has_any_role('Arbiter', 'Bot Meowster')
    async def deltime(self, ctx, timeout: int = None):
        if timeout is None:
            await ctx.send(f'Current auto-delete time is {self.vc_delete_time} seconds.')
        else:
            self.vc_delete_time = timeout
            await ctx.send(f'Changed auto-delete time to {self.vc_delete_time} seconds.')

    @deltime.error
    async def deltime_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Not a valid integer.')

def setup(bot):
    bot.add_cog(Admin(bot))
    print('Admin cog successfully added.')