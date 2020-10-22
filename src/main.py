import discord, asyncio, json

class PorkchopBot(discord.Client):

	def __init__(self):
		super().__init__()

		with open('config.json', 'r') as file:
			self.settings = json.load(file)
		print(self.settings)

		self.run(self.settings['Discord']['Token'])
		print("Bot started...")

	async def on_ready(self):
		print("Bot ready...")


	async def on_message(self, message):
		if message.author == self.user:
			return

		await message.channel.send("This is a test message")


if __name__ == '__main__':
  bot = PorkchopBot()