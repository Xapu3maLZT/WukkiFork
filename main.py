import os
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix=("."), intents=disnake.Intents.all())

#  Load extension function in cog-file
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

# Unload extension function in cog-file
@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")

# Reload extension function in cog-file
@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")

# Check the cogs folder and the extension
for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run = ("#")