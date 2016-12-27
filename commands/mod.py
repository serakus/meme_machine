import discord
from discord.ext import commands
from util import checks
from util.util import log


class mod:

	def __init__(self, bot):
		self.bot = bot
		self.muted = []

	@commands.command()
	@checks.check()
	async def mute(self, name):
		log('Muting {0}'.format(name))
		m = self.find_member(name)
		if m is None:
			await self.bot.say('No player with that name!')
			return
		else :
			self.muted.append(m)
			await self.bot.say('Muting {0}'.format(name))
			while m in self.muted:
				end = await self.bot.wait_for_message(author=m)
				log(end.content)
				if not end.channel.is_private and m in self.muted:
					await self.bot.delete_message(end)

	@commands.command()
	@checks.check()
	async def unmute(self, name):
		log('Unmuting {0}'.format(name))
		m = self.find_member(name)
		if m is None:
			await self.bot.say('No player with that name!')
		else:
			self.muted.remove(m)

	@commands.command()
	@checks.check()
	async def purge(self, channel, name, limit):
		member = self.find_member(name)
		c = self.find_channel(channel)
		if member is None:
			await self.bot.say('No player with that name!')
		else:
			if c is None:
				await self.bot.say('No channel with that name!')
			else:
				def is_author(m):
					return m.author == member
				l = int(limit)
				log('Trying to delete {0} from {1} in {2}'.format(l, name, c.name))
				deleted = await self.bot.purge_from(c, limit=l, check=is_author)
				await self.bot.say('Deleted {} message(s)'.format(len(deleted)))

	def find_member(self, name):
		m = discord.utils.find(lambda m: m.name == name, self.bot.get_all_members())
		if m is None:
			m = discord.utils.find(lambda m: m.nick == name, self.bot.get_all_members())
			if m is None:
				log('Could not find the player')
				return m
		if m.name == self.bot.user.name:
			return None
		return m

	def find_channel(self, name):
		m = discord.utils.find(lambda m: m.name == name, self.bot.get_all_channels())
		if m is None:
			log('Could not find the channel')
		return m


def setup(bot):
	bot.add_cog(mod(bot))
