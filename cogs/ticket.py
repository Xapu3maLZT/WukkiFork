import disnake
from disnake.ext import commands
from disnake.ui import View, button, Select
from disnake.ui.select import SelectOption
from disnake import TextChannel

GUILD_ID = 998809413508939836
CHANNEL_ID = 1076354681569280000
MESSAGE_ID = 1077344063520526366



def setup(bot):
    bot.add_cog(Ticket(bot))
