import discord
import asyncio
from discord.ext import commands
from responses.message_processor import message_processor
from util.util import log
from util.util import load_json
import sys

bot = commands.Bot(command_prefix='!')
proc = message_processor(bot, load_json('responses/responses.json'))


@bot.event
async def on_ready():
    log('Logged in as {0.user.name}'.format(bot))


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if not message.content.startswith('!') and bot.user.mention in message.content:
        await proc.process_message(message)
    else:
        await bot.process_commands(message)

if __name__ == '__main__':
    config = load_json('config.json')
    bot.command_prefix = config['prefix']
    bot.load_extension('commands.admin')
    bot.load_extension('commands.raffle')
    bot.load_extension('commands.mod')
    bot.run(config['token'])
