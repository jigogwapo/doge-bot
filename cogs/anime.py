import datetime as dt
import asyncio
from discord.ext import commands, tasks

starden_genchannel_id = 758361018233126936
aotsundayvid_link = 'https://streamable.com/j65qmq'

class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.aotsunday.start()

    @commands.command()
    @commands.dm_only()
    async def postaotsunday(self, ctx):
        starden_genchannel = self.bot.get_channel(starden_genchannel_id)
        await starden_genchannel.send(aotsundayvid_link)

    @tasks.loop(hours=24*7)
    async def aotsunday(self):
        starden_genchannel = self.bot.get_channel(starden_genchannel_id)
        await starden_genchannel.send(aotsundayvid_link)

    @aotsunday.before_loop
    async def before_aotsunday(self):
        for _ in range(7):
            timenow = dt.datetime.now()
            # check if Sunday
            if timenow.weekday() == 6:
                # loop every 10 seconds through 48 hours after Sunday
                print('Detected that today is Sunday. Starting 48-hr check loop.')
                for _ in range(6*60*48):
                    # check if current time is 6:00 AM
                    if timenow.weekday() == 0 and timenow.hour == 6 and timenow.minute == 0:
                        print('Starting AOT Monday loop.')
                        break
                    await asyncio.sleep(10)
                break
            # wait 24 hours
            await asyncio.sleep(24*60*60)

def setup(bot):
    bot.add_cog(Anime(bot))
    print('Anime cog successfully added.')
