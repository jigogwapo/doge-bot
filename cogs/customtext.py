from discord.ext import commands
from models.CustomTextCommand import CustomCommand
from helpers.custom_text_helpers import create_command, edit_command

class CustomText(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role('Arbiter', 'Bot Meowster', 'Gatekeeper', 'Ambassador')
    async def addcommand(self, ctx, arg):
        await ctx.send(f'Please enter the custom text for the `{arg}` command:')

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        message = await self.bot.wait_for("message", check=check)
        create_command(command_text=arg, custom_text=message.content)
        @commands.command(name=arg)
        async def foo(ctx):
            await ctx.send(message.content)
        self.bot.add_command(foo)
        await ctx.send(f'Successfully added `{arg}` command.')

    @commands.command()
    @commands.has_any_role('Arbiter', 'Bot Meowster', 'Gatekeeper', 'Ambassador')
    async def editcommand(self, ctx, arg):
        await ctx.send(f'Please enter the new custom text for the `{arg}` command:')

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        message = await self.bot.wait_for("message", check=check)
        edit_command(command_text=arg, new_custom_text=message.content)
        command = self.bot.get_command(arg)
        async def foo(ctx):
            await ctx.send(message.content)
        command.callback = foo
        await ctx.send(f'Successfully edited `{arg}` command.')

def setup(bot):
    bot.add_cog(CustomText(bot))
    print('CustomText cog successfully added.')