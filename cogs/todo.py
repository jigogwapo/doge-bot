from discord.ext import commands
import random
from helpers.todo_helpers import add_todo, delete_all_todos, delete_todo, get_todos, create_user, set_all_done, set_todo_done
from helpers.general_helpers import record_usage
from models.User import User

class Todo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    todo_emojis = [
        '<:linus_gun:761509258499981342>',
        '<:yellingwoman:758971086137982976>',
        '<a:weewoo_siren:791201257532030976>',
        '<:starden_CutieYodaGun:793922870601318400>',
        '<a:doggiehi:791200715883937792>'
    ]

    todo_flavortexts = [
        'Oi {}! Eto yung mga kailangan mong gawin:\n',
        '{}, gawin mo to:\n',
        'Sana di makalimutan ni {} na gawin ang mga to:\n',
        'Eto ang listahan mo, {}:\n'
    ]

    @commands.before_invoke(record_usage)
    @commands.group(brief='Show a list of your todos. Use *help td for subcommands.', aliases= ['todo'])
    async def td(self, ctx):
        if ctx.invoked_subcommand is None:
            discord_id = ctx.author.id
            name = ctx.author.name
            if not User.objects(discord_id=discord_id):
                create_user(discord_id)
            todo_list = get_todos(discord_id)
            if todo_list == []:
                await ctx.send('You have no todos yet. Add one using `*td add <your todo>`.')
            else:
                text = random.choice(Todo.todo_flavortexts)
                content = text.format(name)
                content += '>>> '
                for i, todo in enumerate(todo_list):
                    if todo.done:
                        content += f'{i+1} - ~~{todo.content}~~ :white_check_mark:\n'
                    else:
                        content += f'{i+1} - {todo.content}\n'
                emoji = random.choice(Todo.todo_emojis)
                await ctx.send(emoji)
                await ctx.send(content)
        await ctx.message.delete(delay=5)

    @td.command(brief='Add an item to your todo list.')
    async def add(self, ctx, *, todo_content):
        discord_id = ctx.author.id
        if not User.objects(discord_id=discord_id):
            create_user(discord_id)
        add_todo(discord_id, todo_content)
        await ctx.send(f'Added *{todo_content}* to your todos.', delete_after=10)
        await ctx.message.delete(delay=5)

    @td.command(brief='Set a todo item as done or vice versa.')
    async def done(self, ctx, *, args):
        discord_id = ctx.author.id
        if args == 'all':
            set_all_done(discord_id)
            await ctx.send('Set all todos to done.', delete_after=10)
        else:
            try:
                todo_num = int(args)
                todo = set_todo_done(discord_id, todo_num)
                if todo.done:
                    await ctx.send(f'Set *{todo.content}* to done.', delete_after=10)
                else:
                    await ctx.send(f'Set *{todo.content}* to ongoing.', delete_after=10)
            except:
                await ctx.send('Invalid argument.', delete_after=10)
        await ctx.message.delete(delay=5)


    @td.command(aliases=['del'], brief='Delete a todo item.')
    async def delete(self, ctx, *, args):
        discord_id = ctx.author.id
        if args == 'all':
            delete_all_todos(discord_id)
            await ctx.send(f'Deleted all todos.', delete_after=10)
        else:
            try:
                todo_num = int(args)
                todo = delete_todo(discord_id, todo_num)
                await ctx.send(f'Deleted *{todo.content}*.', delete_after=10)
            except:
                await ctx.send('Invalid argument.', delete_after=10)
        await ctx.message.delete(delay=5)

def setup(bot):
    bot.add_cog(Todo(bot))
    print('Todo cog successfully added.')