from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    starden_server_id = 758361018233126932
    starden_anonchannel_id = 789854981981077514
    starden_testchannel_id = 780701253280727040

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

def setup(bot):
    bot.add_cog(Admin(bot))
    print('Admin cog successfully added.')