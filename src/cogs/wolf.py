import discord
import sys
import traceback
import logging
import typing
from discord.ext import commands
from bot import *
import json
import wolframalpha


class Wolf(commands.Cog):
    """Wolframalpha commands"""


    def __init__(self, client, config):
        self.client = client
        self.config = config


    @commands.command(aliases=['wlf'])
    async def wolf(self, ctx, *, question : str):
        """Ask your question in english"""

        app_id="YKTGG4-WKGTEH8VXV"
        wolfi=wolframalpha.Client(app_id)
        res=wolfi.query(question)
        answer=next(res.results).text
        await ctx.send(answer)

def setup(client):
    client.add_cog(Wolf(client, cfg))
