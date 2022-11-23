import disnake
from disnake.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.Cog.listener()
async def on_ready(self):
    print(f"Bot {self.bot.user} is ready to work")

@commands.command()
async def profile(self, ctx):
    await ctx.reply("Test User command")

def setup(bot):
    bot.add_cog(HelpCommand(bot))