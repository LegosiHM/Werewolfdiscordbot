import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from config.config import *


class Game(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def start(self, ctx):
        await ctx.send('Game has started!')
        Night = True
        Day = False
        while gameend is False:
            if Night:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
                source1 = FFmpegPCMAudio('Nightsound_2.wav')
                player = voice.play(source1)
                Day = True
                Night = False
            elif Day is True:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
                source2 = FFmpegPCMAudio('Morningsound_1.wav')
                player = voice.play(source2)
                Day = False
                Night = True

            else:
                await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command")

    @commands.command()
    async def game(self, ctx):
        game = discord.Embed(color=0x000066)
        game.add_field(name="Villagers", value=":bust_in_silhouette:" * user["userrole"].count('werewolf'), inline=True)
        game.add_field(name="Living players", value=' \n'.join(user["username"]), inline=True)
        game.add_field(name="Day", value="1", inline=True)
        game.add_field(name="Werewolfs", value=":wolf:" * user["userrole"].count('villager'), inline=False)
        await ctx.send(embed=game)


def setup(client):
    client.add_cog(Game(client))
