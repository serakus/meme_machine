from discord.ext import commands
from util import checks
from util.util import log
from datetime import datetime
import discord
import random

class raffle:

    def __init__(self, bot):
        self.bot = bot
        self.started = False
        self.time = 0
        self.desc = ''
        self.now = datetime.now()
        self.members = []

    @commands.command(name='raffle-start', pass_context=True)
    async def start(self, ctx, time, desc):
        if self.started:
            await self.bot.say('A raffle has already been started! Join now!')
        else:
            self.started = True
            self.desc = desc
            def end_check(m):
                return False
            self.time = float(time)*60
            self.now = datetime.now()
            self.members = []
            await self.bot.say('Raffle "{0}" is starting! You have {1} min left to join!'.format(desc, time))
            end = await self.bot.wait_for_message(timeout=self.time, author=ctx.message.author, check=end_check)
            if end is None and self.started:
                self.started = False
                await self.bot.say('Raffle "{0}" has ended! {1} won the raffle!'.format(self.desc, random.choice(self.members).mention))

    @commands.command(pass_context=True)
    async def enter(self, ctx):
        if self.started and ctx.message.author not in self.members:
            self.members.append(ctx.message.author)
            diff = datetime.now() - self.now
            left = self.time - diff.seconds
            unit = 'seconds'
            if left > 60:
                left = left / 60
                unit = 'min'
            await self.bot.say('{0.mention} entered the raffle! {1} {2} left to enter the raffle!'.format(ctx.message.author, int(left), unit))
        else:
            if not self.started:
                await self.bot.say('There is currently no raffle!')
            else:
                await self.bot.say('{0}, you already joined the raffle!'.format(ctx.message.author.mention))

def setup(bot):
    bot.add_cog(raffle(bot))
