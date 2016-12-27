from discord.ext import commands
import discord.utils

list = []


def is_owner_check(message):
    return message.author.id == '151409406205100042'


def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))

def check():
    return commands.check(lambda ctx:has_permissions(ctx.message))

def has_permissions(ctx):
    if is_on_list(ctx) or is_owner_check(ctx):
        return True
    return False

def is_on_list(ctx):
    if ctx.author.name in list:
        return True
    return False

def check_permissions(ctx, perms):
    msg = ctx.message
    if is_owner_check(msg):
        return True
    return False
