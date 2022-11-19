import os
import disnake

from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())

@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("ХУЙ")

bot.load_extension("cogs.stats")

TOKEN = os.environ["TOKEN"]
bot.run=(TOKEN)
