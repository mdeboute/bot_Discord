import discord
import sys
import traceback
import logging
import typing
from discord.ext import commands
from bot import *
import json


class Admin(commands.Cog):
    """Administrator commands"""


    def __init__(self, client, config):
        self.client = client
        self.config = config

    #Command
    @commands.command(aliases=['clr'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount):

        nb=0
        if amount=='all':
            nb=-1
        else:
            nb=int(amount)
        if nb==-1:
            await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=nb+1)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, members: commands.Greedy[discord.Member], *, reason: str):
        for member in members:
            await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, members: commands.Greedy[discord.Member], delete_days: typing.Optional[int] = 0, *, reason: str):
        for member in members:
            await member.ban(delete_message_days=delete_days, reason=reason)

    @commands.command(aliases=['uban'])
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users=await ctx.guild.bans()
        member_name, member_discriminator=member.split("#")
        for ban_entry in banned_users:
            user=ban_entry.user
            if (user.name, user.member_discriminator)==(member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

    @commands.command(aliases=['dlinv'])
    @commands.has_permissions(administrator=True)
    async def del_invite(self, ctx):
        invites=await ctx.guild.invites()
        for i in invites:
            await i.delete()

    @commands.command(aliases=['inf'])
    async def info(self, ctx, *, member: discord.Member):

        fmt = '{0} joined on {0.joined_at} and has {1} roles.'
        await ctx.send(fmt.format(member, len(member.roles)))

    @commands.command(aliases=['toprole'])
    async def show_toprole(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.message.author

        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')

    @commands.command(aliases=['perms_for', 'permissions', 'perms'])
    async def check_permissions(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.message.author

        # Here we check if the value of each permission is True.
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        # And to make it look nice, we wrap it in an Embed.
        embed = discord.Embed(title='Permissions for:', description=member.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        # \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
        embed.add_field(name='\uFEFF', value=perms)

        await ctx.send(embed=embed)

    @commands.command(aliases=['ld'])
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        client.load_extension(f"cogs.{extension}")

    @commands.command(aliases=['unld'])
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        client.unload_extension(f"cogs.{extension}")

    @commands.command(aliases=['reld'])
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")

    @commands.command(aliases=['change_p'])
    @commands.has_permissions(administrator=True)
    async def change_prefix(self, ctx, prefix):
        with open("./src/prefixes.json", "r") as f:
            prefixes=json.load(f)
        prefixes[str(ctx.guild.id)]=prefix
        with open("./src/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        await ctx.send(f"The new prefix command is now : {prefix}")


def setup(client):
    client.add_cog(Admin(client, cfg))
