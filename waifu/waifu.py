"""Wafu cog.  Send waifu.pics to a channel."""
import asyncio
import discord
import requests
from redbot.core import checks, Config, commands
from redbot.core.bot import Red

#Global variables
URL = "https://api.waifu.pics/sfw/"

class Waifu(commands.cog):
    """Display waifu.pic pictures"""

    def __init__(self, bot: Red):
        self.bot = bot

    def waifuCmd(self, ctx, imageType):
        """Display a waifu.pic picture"""
        await ctx.channel.trigger_typing()

    # [p]waifu
    @commands.command(name="waifu")
    async def _waifu(self, ctx, imageType: str = None):
        """Display a random waifu"""
        if not imageType:
            imageType = "waifu"
        
        await self.waifuCmd(ctx, )


    def getImage(image, title):
        """
        Take a passed url from Waifu.pics, and construct a discord.Embed object

        Parameters:
        -----------
        image : a URL
        title: a string

        Returns:
        -----------
        embed : discord.embed
            a fully constructed discord.Embed object, ready to be sent as a message.
        """
        embed = discord.Embed()
        embed.colour = discord.Colour.red()
        embed.title = title
        embed.url = image
        embed.set_image(url=image)
        return embed
