import discord
import asyncio
from discord.ext import commands
import message_processor
from util import log
from util import load_json

bot = commands.Bot(command_prefix='!')
proc = message_processor.message_processor(bot, load_json('responses.json')['random'])

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.NoPrivateMessage):
        await bot.send_message(ctx.message.author, 'This command cannot be used in private messages.')
    elif isinstance(error, commands.DisabledCommand):
        await bot.send_message(ctx.message.author, 'Sorry. This command is disabled and cannot be used.')
    elif isinstance(error, commands.CommandInvokeError):
        print('In {0.command.qualified_name}:'.format(ctx), file=sys.stderr)
        traceback.print_tb(error.original.__traceback__)
        print('{0.__class__.__name__}: {0}'.format(error.original), file=sys.stderr)

@bot.event
async def on_ready():
    log('Logged in as {0.user.name}'.format(bot))

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if not message.content.startswith('!') and bot.user.mention in message.content :
        await proc.process_message(message)
    else :
        await bot.process_commands(message)

if __name__ == '__main__':
    config = load_json('config.json')
    bot.command_prefix = config['prefix']
    #bot.load_extension('message_processor')
    bot.run(config['token'])
