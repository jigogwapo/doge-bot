from discord.ext import commands
from discord.utils import get
import asyncio
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc_delete_time = 1200

    starden_server_id = 758361018233126932
    starden_anonchannel_id = 789854981981077514
    starden_testchannel_id = 780701253280727040
    starden_voicechatchannel_id = 798943215008088155
    starden_genchannel_id = 758361018233126936

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot connected as {self.bot.user}')

    @commands.Cog.listener()
    async def on_message(self, message):
        starden_server = self.bot.get_guild(Admin.starden_server_id)
        if not message.guild: # for solo dms
            if message.content.startswith('*anon') and starden_server.get_member(message.author.id) is not None:
                starden_anonchannel = self.bot.get_channel(Admin.starden_anonchannel_id)
                anon_message = message.content[6:]
                await starden_anonchannel.send(f'**anon**: {anon_message}')
                await message.channel.send(f'anon message successfully sent. you can now delete your DM.')

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
            starden_genchannel = self.bot.get_channel(Admin.starden_anonchannel_id)
            tarodancers = [
                '<a:ztarden_TaroDanceSam:800943071545655346>',
                '<a:ztarden_TaroDanceCarrie:800952631165059122>',
                '<a:ztarden_TaroDanceErn:800954713113493514>'
                '<a:ztarden_TaroDancePrei:800947555210756136>',
                '<a:ztarden_TaroDanceManny:800947552458768425>',
                '<a:ztarden_JujuTaroDance:801241457474142228>'
                '<a:ztarden_TaroDanceKing:801239042012086283>',
                '<a:ztarden_TaroDanceGold:800950085344952352>',
                '<a:ztarden_TaroDanceGeros:801239041625686037>',
                '<a:ztarden_TaroDanceElder:801239041701052426>'
            ]
            await starden_genchannel.send(''.join(tarodancers))
            await starden_genchannel.send(f'Welcome new ket {member.mention}! I\'m Doge.')

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