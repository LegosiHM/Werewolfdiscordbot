import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"User {member} has been kicked")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to kick member")


def setup(client):
    client.add_cog(Kick(client))
