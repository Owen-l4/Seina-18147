from discord.ext import commands
from discordTogether import DiscordTogether

class YoutubeTogether(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.togetherControl = DiscordTogether(bot)
    
    @commands.command()
    async def YoutubeTogether(self, ctx):
        try:
            link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
            await ctx.message.delete()
            await ctx.send(f"click the link to join the\n{link}")
        except:
            await ctx.send("you are not in a voice channel")

def setup(bot):
    bot.add_cog(YoutubeTogether(bot))