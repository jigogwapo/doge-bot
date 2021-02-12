async def record_usage(ctx, *args):
    print(ctx.author, 'used', ctx.command, 'at', ctx.message.created_at)