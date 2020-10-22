import discord, asyncio, json

class PorkchopBot(discord.Client):

	def __init__(self):
		super().__init__()

		with open('config.json', 'r') as file:
			self.settings = json.load(file)
		print(self.settings)

		self.run(self.settings['Discord']['token'])
		print("Bot started...")

	async def on_ready(self):
		print("Bot ready...")


	async def on_message(self, message):
		if message.author == self.user:
			return

		if message.content[0] == '!':
			if 'purge' in message.content:
				await self.purge(message, 10)
		elif message.content[0] == '?':
			await message.channel.send("This is a question")

	async def purge (self, message, range):
		  """
		  This function purges messages from the message channel.
		  :param message: The recieved command.
		  :param range: The amount of messages to delete.

		  TODO: Implement the range functionality.
		  """

	  	range = int(range)
	  	message_counter = 0

	  	async for msg in message.channel.history(limit=range):
	  		await msg.delete()
	  		message_counter +=1
	  	print(f'deleted {message_counter} messages from {message.channel}!')


if __name__ == '__main__':
  bot = PorkchopBot()