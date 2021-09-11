import discord
from discord import activity
from discord.ext import commands
from discord import Game

from BotCore import BotCore

class BasicFunctions(BotCore):
    @commands.Cog.listener()
    async def on_ready(self):
        print(">>bot online<<")

    @commands.command()
    async def ping(self,ctx):
        embed=discord.Embed(title="Pong!",description=f'{round(self.bot.latency*1000)} ms', color=0xa7f21c)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(BasicFunctions(bot))