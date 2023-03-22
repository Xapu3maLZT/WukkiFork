import disnake
import openai
import json
import os

from disnake.ext import commands

class OpenAI(commands.Cogs):
    def __init__(self, bot):
        self.bot = bot
        open.ai_key = "settings.json"


def setup(bot):
    bot.add_cog(openai(bot))