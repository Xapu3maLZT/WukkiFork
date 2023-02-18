import json
import disnake
from disnake.ext import commands

# Load settings from file
with open('settings.json') as f:
    settings = json.load(f)

bot = commands.Bot(command_prefix=(".",), intents=disnake.Intents.all())

# Load extensions (cogs) from list in settings
for extension in settings["cogs"]:
    bot.load_extension(extension)

bot.run(settings["token"])