import yaml
import os
import disnake
from disnake.ext import commands
from disnake import Embed, ActionRow, Button, ButtonStyle

class Timings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def timing(self, ctx, *args):
    author = ctx.author
    timings_embed = disnake.Embed(
        description="Это не магические значения. Многие из этих параметров имеют реальные последствия для механики вашего сервера\. Смотрите [это руководство](https://eternity.community/index.php/paper-optimization/) для подробной информации о функциональности каждой настройки.",
        footer={"text": f"По запросу {author}", "icon_url": author.avatar_url}
    )
    url = None
    fields = []


def setup(bot):
    bot.add_cog(Timings(bot))