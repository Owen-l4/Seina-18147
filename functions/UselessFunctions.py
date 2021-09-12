import discord
from discord.ext import commands


from random import randint
import math
from PIL import Image, ImageDraw


from BotCore import BotCore

class UselessFunctions(BotCore):
    @commands.command()
    async def color(self,ctx):

        r,g,b = [randint(0,255) for i in range(3)]

        color_str = "#"
        for i in [r,g,b]:
            color_str += hex(i)[2:].upper()


        img = Image.new("RGB", (300,300) ,(r,g,b))
        img.save("color.jpg")


        embed = discord.Embed(title="Seina pick a color for you", description = color_str, color=discord.Color.from_rgb(r,g,b)) 
        file = discord.File("color.jpg", filename="color.jpg")
        embed.set_image(url=f"attachment://color.jpg")
        await ctx.send(embed=embed , file = file)
    
    @commands.command()
    async def pop(self,ctx,word='pop',width=10,height=10):

        if (len(word) + 4)*width*height > 1000:
            await ctx.send("oops, the pop is too big")
        else:
            await ctx.message.delete()

            embed = discord.Embed(title="Seina give you a bubble paper", description = (('||'+word+'||')*width+'\n')*height, color = 0xffffff) 
            await ctx.send(embed = embed)
        





def setup(bot):
    bot.add_cog(UselessFunctions(bot))