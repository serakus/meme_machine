import asyncio
from util import log
import random

class message_processor:

    def __init__(self, bot, responses):
        self.bot = bot
        self.responses = responses

    async def process_message(self, message):
        if 'rate' in message.content :
            await self.reply('{0}/10'.format(random.randint(0,10)), message)
        else :
            await self.reply(random.choice(self.responses), message)

    async def reply(self, message, ctx):
        log('Responding to {0.name}'.format(ctx.author))
        msg = '{0.mention} ' + message
        await self.bot.send_message(ctx.channel, msg.format(ctx.author))
