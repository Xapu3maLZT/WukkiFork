import disnake
from disnake.ext import commands

class TicketSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ticket(self, ctx, *, subject):
        category = disnake.utils.get(ctx.guild.categories, name='Тикеты')
        channel = await ctx.guild.create_text_channel(name=f'ticket-{ctx.author.display_name}', category=category)

        await channel.set_permissions(ctx.guild.default_role, read_messages=False)
        await channel.set_permissions(ctx.author, read_messages=True, send_messages=True)

        embed = disnake.Embed(title=f'Новый тикет от {ctx.author.display_name}', description=subject)
        embed.set_footer(text='Связаться с администратором, нажмите на реакцию 👍')
        msg = await channel.send(embed=embed)

        await msg.add_reaction('👍')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if not payload.guild_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        if payload.emoji.name != '👍':
            return

        if message.author != self.bot.user:
            return

        for reaction in message.reactions:
            if reaction.emoji != '👍':
                continue

            users = await reaction.users().flatten()
            if self.bot.user in users:
                continue

            await channel.set_permissions(payload.member, read_messages=True, send_messages=True)
            await message.remove_reaction('👍', self.bot.user)

def setup(bot):
    bot.add_cog(TicketSystem(bot))
