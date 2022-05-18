import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord import member
from discord import FFmpegPCMAudio, Profile
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os
from discord.utils import get
import random
from config.config import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=PREFIX, intents=intents)


@client.event
async def on_ready():
    print("Bot is ready")
    print("------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello")


username = []

@client.command()
async def join(ctx):
    name = ctx.author.name
    username.append(name)
    print(username)
    await ctx.send(f"Hello {ctx.author.name}")

print(username)
#async def join_game(ctx, member: discord.User):
#    name = member.display_name
#    username.append(name)
#    await ctx.send(f'{member} has joined the game!')

client.run(TOKEN)