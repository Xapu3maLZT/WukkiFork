import disnake
import openai
import json
import os

from disnake.ext import commands

class OpenAI(commands.Cogs):
    def __init__(self, bot):
        self.bot = bot
        open.ai_key = "settings.json"

@commands.command()
async def openai(self, ctx, *, prompt):
    completions = openai.Completion.create(
        engine = 'davinci',
        prompt=prompt,
        max_tokens=100
    )
    message = completions.choices[0].text
    await ctx.send(message)

def setup(bot):
    bot.add_cog(openai(bot))