from discord.ext import commands
import discord.utils


def is_owner_check(message):
    return message.author.id == '151409406205100042'


def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))


def check_permissions(ctx, perms):
    msg = ctx.message
    if is_owner_check(msg):
        return True
    return False
