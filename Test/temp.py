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


@client.command()
async def addrole(ctx):
    await ctx.send('Check out your role!, by write !myrole @(your name)')
        for i in range(len(username)):
            userrole.append(random.choice(role))
            if userrole.count('werewolf') >= ((len(userrole)//2)+1):
                userrole[random.randint(0,len(username-1))] = 'villager'
        print(userrole)


# เช็คบอททำงานมั้ย
@client.event
async def on_ready():
    print(f'{client.user} is Ready')


# เข้าร่วมเกม
@client.command()
async def join_game(ctx, member: discord.User):
    name = member.display_name
    username.append(name)
    await ctx.send(f'{member} has joined the game!')
    print(username)


# คำสั่งเริ่มเกม(!start)
@client.command(pass_context=True)
async def start(ctx):
    await ctx.send('Game has started!')
    Night = True
    Day = False
    while gameend == False:
        if Night:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source1 = FFmpegPCMAudio('Nightsound_2.wav')
            player = voice.play(source1)
            Day = True
            Night = False
        elif Day == True:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source2 = FFmpegPCMAudio('Morningsound_1.wav')
            player = voice.play(source2)
            Day = False
            Night = True

        else:
            await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command")


# คำสั่งบอทเข้าช่องพูดคุย (!join)
@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel")


# คำสั่งบอทออกช่องพูดคุย (!leave)
@client.command(pass_context=True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("I am not in a voice channel")


# Kick User
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to kick member')


# !game
@client.command()
async def game(ctx):
    game = discord.Embed(color=0x000066)
    game.add_field(name="Villagers", value=":bust_in_silhouette:" * userrole.count('werewolf'), inline=True)
    game.add_field(name="Living players", value=' \n'.join(username), inline=True)
    game.add_field(name="Day", value="1", inline=True)
    game.add_field(name="Werewolfs", value=":wolf:" * userrole.count('villager'), inline=False)
    await ctx.send(embed=game)


@client.command()
async def kill(ctx, member: discord.Member):
    name = member.display_name
    position_role = username.index(name)
    user_role = userrole[position_role]
    if user_role == 'villager':
        await ctx.send('You can not kill because you are villager :bust_in_silhouette: ')
    elif user_role == 'werewolf':
        name = member.display_name
        position = username.index(name)
        killed = username.pop(position)
        await ctx.send(f'{killed} has been killed :skull:')


@client.command()
async def command(ctx):
    command = discord.Embed(title="Werewolf commands")
    command.add_field(name="Starting a game", value="!join_game @(your name)\n"
                                                    "!addrole\n"
                                                    "!myrole @(your name)\n"
                                                    "!start")
    command.add_field(name="In game", value="!game\n"
                                            "!kill")
    await ctx.send(embed=command)


#!want_help
@client.command()
async def want_help(ctx):
    want_help = discord.Embed(title="How to play")
    want_help.add_field(name="Step1:Join game", value="You and your friends need to write !join_game @(your name)",
                        inline=False)
    want_help.add_field(name="Step2:Add role", value="Someone need to write !addrole to put role to everybody", inline=False)
    want_help.add_field(name="Step3:Check role", value="You need to write !myrole @(your name) to see your role", inline=False)
    want_help.add_field(name="Step4:Start", value="Someone need to write !start to start the game", inline=False)
    want_help.add_field(name="Check game", value="You guys can check the game that how many Living players are there, Villagers,Werewolfs,Day by write !game", inline=False)
    await ctx.send(embed=want_help)


#check role !myrole
@client.command()
async def myrole(ctx, user: discord.User):
    name = str(user.display_name)
    position_role = int(username.index(name))
    user_role = userrole[position_role]
    message = f"Your role is {user_role}"
    await user.send(message)



client.run(TOKEN)