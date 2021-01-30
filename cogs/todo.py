from discord.ext import commands
from helpers.todo_helpers import add_todo, delete_all_todos, delete_todo, get_todos, create_user, set_all_done, set_todo_done, User

class Todo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(brief='Show a list of your todos. Use *help td for subcommands.')
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
                content = f'{name}\'s todos:\n'
                content += '>>> '
                for i, todo in enumerate(todo_list):
                    if todo.done:
                        content += f'{i+1} - ~~{todo.content}~~ :white_check_mark:\n'
                    else:
                        content += f'{i+1} - {todo.content}\n'
                await ctx.send(content)

    @td.command(brief='Add an item to your todo list.')
    async def add(self, ctx, *, todo_content):
        discord_id = ctx.author.id
        if not User.objects(discord_id=discord_id):
            create_user(discord_id)
        add_todo(discord_id, todo_content)
        await ctx.send(f'Added *{todo_content}* to your todos.')

    @td.command(brief='Set a todo item as done or vice versa.')
    async def done(self, ctx, *, args):
        discord_id = ctx.author.id
        if args == 'all':
            set_all_done(discord_id)
            await ctx.send('Set all todos to done.')
        else:
            try:
                todo_num = int(args)
                todo = set_todo_done(discord_id, todo_num)
                if todo.done:
                    await ctx.send(f'Set *{todo.content}* to done.')
                else:
                    await ctx.send(f'Set *{todo.content}* to ongoing.')
            except:
                await ctx.send('Invalid argument.')


    @td.command(aliases=['del'], brief='Delete a todo item.')
    async def delete(self, ctx, *, args):
        discord_id = ctx.author.id
        if args == 'all':
            delete_all_todos(discord_id)
            await ctx.send(f'Deleted all todos.')
        else:
            try:
                todo_num = int(args)
                todo = delete_todo(discord_id, todo_num)
                await ctx.send(f'Deleted *{todo.content}*.')
            except:
                await ctx.send('Invalid argument.')

def setup(bot):
    bot.add_cog(Todo(bot))
    print('Todo cog successfully added.')