import disnake
from disnake.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

pass

def setup(bot):
    bot.add_cog(Moderation(bot))