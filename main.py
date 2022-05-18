import discord
from discord.ext import commands
from config.config import *
import os

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=PREFIX, intents=intents)


# Bot is ready
@client.event
async def on_ready():
    print(f'{client.user} is Ready')

initial_extenions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extenions.append("cogs."+filename[:-3])

if __name__ == '__main__':
    for extension in initial_extenions:
        client.load_extension(extension)


client.run(TOKEN)
