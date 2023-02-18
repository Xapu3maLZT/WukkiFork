import json
import disnake
from disnake.ext import commands

with open('settings.json') as f:
    settings = json.load(f)

bot = commands.Bot(command_prefix=(".",), intents=disnake.Intents.all())

for extension in settings["cogs"]:
    bot.load_extension(extension)

bot.run(settings["token"])