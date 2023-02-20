import disnake
from disnake.ext import commands
from disnake.ui import View, button, Select
from disnake.ui.select import SelectOption
from disnake import TextChannel

GUILD_ID = 998809413508939836
CHANNEL_ID = 1076354681569280000
MESSAGE_ID = 1077344063520526366

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.bot.get_guild(GUILD_ID)
        channel = guild.get_channel(CHANNEL_ID)
        message = await channel.fetch_message(MESSAGE_ID)
        view = TicketView()
        await message.edit(content="Для открытия тикета, нажмите кнопку:", view=view, allowed_mentions=disnake.AllowedMentions.none())

    @commands.command()
    async def ticket(self, ctx):
        await create_ticket(ctx.channel)

class TicketView(View):
    @button(label="Открыть тикет", style=disnake.ButtonStyle.green)
    async def open_ticket(self, button: disnake.Button, interaction: disnake.MessageInteraction):
        await interaction.message.delete()
        await create_ticket(interaction.channel)

async def create_ticket(channel: TextChannel):
    options = [
        SelectOption(label="Проблема с оплатой"),
        SelectOption(label="Техническая проблема"),
        SelectOption(label="Другое")
    ]
    view = View()
    view.add_item(Select(options=options, placeholder="Выберите причину", min_values=1, max_values=1))
    message = await channel.send("Откройте тикет, выбрав причину:", view=view)
    view.message = message

def setup(bot):
    bot.add_cog(Ticket(bot))
