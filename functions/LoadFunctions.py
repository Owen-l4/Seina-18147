import discord
from discord.ext import commands

from BotCore import BotCore

class LoadFunctions(BotCore):
    @commands.command()
    @commands.is_owner()
    async def load(self,ctx,extention):
        self.bot.load_extension(f'functions.{extention}')
        await ctx.message.delete()
        await ctx.send(f'Load function {extention} successfully')
    @commands.command()
    @commands.is_owner()
    async def unload(self,ctx,extention):
        self.bot.unload_extension(f'functions.{extention}')
        await ctx.message.delete()
        await ctx.send(f'Un - Load function {extention} successfully')
    @commands.command()
    @commands.is_owner()
    async def reload(self,ctx,extention):
        self.bot.reload_extension(f'functions.{extention}')
        await ctx.message.delete()
        await ctx.send(f'Re - Load function {extention} successfully')

def setup(bot):
    bot.add_cog(LoadFunctions(bot))