import random
from discord.ext import commands
from config.config import *


class JoinGame(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def joingame(self, ctx):
        name = ctx.author.name
        user["username"].append(name)
        await ctx.send(f"Hello {ctx.author.name}")
        print(ctx.author.name)

    @commands.Cog.listener()
    async def addrole(self, ctx):
        await ctx.send('Check out your role!, by write !myrole @(your name)')

        user["userrole"].append(random.choice(role))
        if user["userrole"].count('werewolf') >= ((len(user["userrole"]) // 2) + 1):
            user["userrole"][random.randint(0, len(user["username"]))] = 'villager'

    @commands.Cog.listener()
    async def myrole(self, ctx):
        name = str(ctx.author.name)
        position_role = int(user["username"].index(name))
        user_role = user["userrole"][position_role]
        message = f"Your role is {user_role}"
        await ctx.author.send(message)


def setup(client):
    client.add_cog(JoinGame(client))
