import disnake
from disnake.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ban(self, ctx, member: disnake.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} был забанен.")

    @commands.slash_command()
    async def mute_text(self, ctx, member: disnake.Member, duration: int, *, reason=None):
        await interaction.response.defer()
        role = disnake.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.text_channels:
                await channel.set_permissions(role, send_messages=False)

        await member.add_roles(role, reason=reason)
        await ctx.send(f"{member} был замучен на {duration} секунд.")

    @commands.slash_command()
    async def mute_voice(self, ctx, member: disnake.Member, duration: int, *, reason=None):
        voice = member.voice
        if not voice:
            await ctx.send("Пользователь не находится в голосовом канале.")
            return

        voice_channel = voice.channel
        overwrite = voice_channel.overwrites_for(member)

        if not overwrite:
            overwrite = disnake.PermissionOverwrite()

        overwrite.update(connect=False, speak=False)
        await voice_channel.set_permissions(member, overwrite=overwrite, reason=reason)

        await ctx.send(f"{member} был замучен на {duration} секунд.")

        await disnake.utils.sleep(duration)
        overwrite.update(connect=True, speak=True)
        await voice_channel.set_permissions(member, overwrite=overwrite, reason="Мут истек.")

def setup(bot):
    bot.add_cog(Moderation(bot))

import disnake
from disnake.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

"""
@commands.slash_command()
    async def ban(self, ctx, member: disnake.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} был забанен.")

    @commands.slash_command()
    async def mute_text(self, ctx, member: disnake.Member, duration: int, *, reason=None):
        await interaction.response.defer()
        role = disnake.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.text_channels:
                await channel.set_permissions(role, send_messages=False)

        await member.add_roles(role, reason=reason)
        await ctx.send(f"{member} был замучен на {duration} секунд.")
"""
