import asyncio

async def paginate(ctx, bot, content_list, *, isEmbed=False):
    if isEmbed:
        message = await ctx.send(embed=content_list[0])
    else:
        message = await ctx.send(content=content_list[0])

    async def edit_message(message, data):
        if isEmbed:
            await message.edit(content=None, embed=data)
        else:
            await message.edit(embed=None, content=data)

    list_len = len(content_list)
    cur_page = 1
    await message.add_reaction('◀')
    await message.add_reaction('❌')
    await message.add_reaction('▶')

    def check_react(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['◀', '❌', '▶']

    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60, check=check_react)

            if str(reaction.emoji) == '◀' and cur_page > 1:
                cur_page -= 1
                await edit_message(message, content_list[cur_page-1])
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == '▶' and cur_page != list_len:
                cur_page += 1
                await edit_message(message, content_list[cur_page-1])
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == '❌':
                await message.delete()
                break

            else:
                await message.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            break

async def add_delete_button(ctx, bot, message):
    await message.add_reaction('❌')

    def check_react(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['❌']

    while True:
        try:
            await bot.wait_for('reaction_add', timeout=60, check=check_react)
            await message.delete()
        except asyncio.TimeoutError:
            break
