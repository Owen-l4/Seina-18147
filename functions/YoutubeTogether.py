from discord.ext import commands
from discordTogether import DiscordTogether

class YoutubeTogether(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.togetherControl = DiscordTogether(bot)
    
    @commands.command()
    async def start(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.send(f"Click the blue link!\n{link}")

def setup(bot):
    bot.add_cog(YoutubeTogether(bot))