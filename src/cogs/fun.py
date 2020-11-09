import discord, random, typing, os, json
from discord.ext import commands
from utils import *
from discord.utils import get
from bot import *



class Fun(commands.Cog):
    """Just somes cool stuff"""


    def __init__(self, client, config):
        self.client = client
        self.config = config

    #Command
    @commands.command(aliases=['pg'])
    async def ping(self, ctx):
        await ctx.send(f"pong 🏓 ({round(self.client.latency * 1000)}ms)")

    @commands.command(aliases=['8ball', '8b'])
    async def _8ball(self, ctx, *, question):
        responses=[
            "Essaye plus tard",
            "Essaye encore",
            "Pas d'avis",
            "C'est ton destin",
            "Le sort en est jeté",
            "Une chance sur deux",
            "Repose ta question",
            "D'après moi oui",
            "C'est certain",
            "Oui absolument",
            "Tu peux compter dessus",
            "Sans aucun doute",
            "Très probable",
            "Oui",
            "C'est bien parti",
            "C'est non",
            "Peu probable",
            "Faut pas rêver",
            "N'y compte pas",
            "Impossible"]
        await ctx.send(f"Question : {question}\nRéponse : {random.choice(responses)}")

    @commands.command()
    async def dm(self, ctx, members: commands.Greedy[discord.Member], *, message: str):
        for member in members:
            if member.dm_channel==None:
                await member.create_dm()
            try:
                await member.send(message,delete_after=3600)
            except discord.Forbidden:
                await ctx.send("Error : " + member + " didn't open his/her DMs 😕")

    @commands.command()
    async def mood(self, ctx, name=None):
        if name==None:
            member=ctx.author.display_name
        else:
            member=name
        color=randomColor()
        img=randomURL()
        description=str(member)+" be like :"
        embed=createEmbed("your mood", description, color, img)
        await ctx.send(embed=embed)

    #@commands.command()
    #async def goulag(self, ctx, members: commands.Greedy[discord.Member], *, reason=None):
    #channel=discord.VoiceChannel
        #channel.name='Goulag'
        #for member in members:
            #await member.move_to(channel=channel, reason=reason)
        #await ctx.send("Member(s) have been goulagized")


def setup(client):
    client.add_cog(Fun(client, cfg))
