import discord
from discord.ext import commands

from BotCore import BotCore

from random import choice

import json

class CustomChat(BotCore):
    @commands.group()
    async def define_message(self,ctx):
        pass

    @define_message.command(
        help="add reply message when message contain the context",
        brief="add reply message when message contain the context"
    )
    async def contain(self,ctx,context,reply_message):
        embed = update_reply("contain",context,reply_message)
        await ctx.send(embed=embed)
    @define_message.command(
        help="add reply message when message equal the context",
        brief="add reply message when message equal the context"
    )
    async def equal(self,ctx,context,reply_message):
        embed = update_reply("equal",context,reply_message)
        await ctx.send(embed=embed)

    @define_message.command(
        help="add reply message when message startwith the context",
        brief="add reply message when message startwith the context"
    )
    async def startwith(self,ctx,context,reply_message):
        embed = update_reply("startwith",context,reply_message)
        await ctx.send(embed=embed)

    @define_message.command(
        help="add reply message when message endwith the context",
        brief="add reply message when message endwith the context"
    )
    async def endwith(self,ctx,context,reply_message):
        embed = update_reply("endwith",context,reply_message)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if not message.content.startswith("http"):
                with open('reply.json','r',encoding='utf8') as file:
                    reply = json.load(file)
                    
                msg = [] 
                for i in reply["contain"].keys():
                    if i.lower() in message.content.lower():
                        msg += reply["contain"][i]
                
                for i in reply["equal"].keys():
                    if i.lower() == message.content.lower():
                        msg += reply["equal"][i]
                
                for i in reply["startwith"]:
                    if message.content.lower().startswith(i.lower()):
                        msg += reply["startwith"][i]
                
                for i in reply["endwith"]:
                    if message.content.lower().endswith(i.lower()):
                        msg += reply["endwith"][i]
                
                if(len(msg) > 0):
                    await message.reply(choice(msg))

def update_reply(mode,context,reply):
    jsonFile = open("reply.json", "r",encoding='utf8') 
    data = json.load(jsonFile)
    jsonFile.close() 

    if context not in data[mode].keys():
        data[mode][context] = []
    if reply not in data[mode][context]:
        data[mode][context].append(reply)

    jsonFile = open("reply.json", "w+",encoding='utf8')
    json.dump(data,jsonFile, indent=4,ensure_ascii=False)
    jsonFile.close()

    embed=discord.Embed(title="reply message", description="the reply you just add", color=0xa7f21c)
    embed.add_field(name=mode, value=f"`{context}`", inline=True)
    embed.add_field(name="reply", value=f"`{reply}`", inline=True)
    return embed

    
def setup(bot):
    bot.add_cog(CustomChat(bot))