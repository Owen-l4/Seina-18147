import discord
from discord.ext import commands

from BotCore import BotCore

class OtherFunctions(BotCore):
    @commands.command()
    async def pop(self,ctx,word='pop',width=10,height=10):
        await ctx.message.delete()
        await ctx.send((('||'+word+'||')*width+'\n')*height)


    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Banned {member.mention}')

        

def setup(bot):
    bot.add_cog(OtherFunctions(bot))