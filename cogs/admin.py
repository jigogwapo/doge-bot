from discord.ext import commands
import asyncio
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc_delete_time = 1200

    starden_server_id = 758361018233126932
    starden_anonchannel_id = 789854981981077514
    starden_testchannel_id = 780701253280727040
    starden_voicechatchannel_id = 798943215008088155

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
            if not message.author.bot:
                await message.reply(f'Message will be deleted in {self.vc_delete_time} seconds.', delete_after=2)
            await asyncio.sleep(self.vc_delete_time-2)
            if not message.author.bot:
                await message.reply(f'Deleting...', delete_after=2)
            await asyncio.sleep(2)
            try:
                await message.delete()
            except:
                pass

    @commands.command(brief='mod command to change vc auto-delete time')
    @commands.has_any_role('Arbiter', 'Bot Master')
    async def deltime(self, ctx, timeout: int = None):
        if timeout is None:
            await ctx.send(f'Current auto-delete time is {self.vc_delete_time} seconds.', delete_after=2)
        else:
            self.vc_delete_time = timeout
            await ctx.send(f'Changed auto-delete time to {self.vc_delete_time} seconds.', delete_after=2)

    @deltime.error
    async def deltime_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Not a valid integer.')

def setup(bot):
    bot.add_cog(Admin(bot))
    print('Admin cog successfully added.')