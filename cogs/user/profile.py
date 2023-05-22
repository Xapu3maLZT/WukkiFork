import disnake
from disnake.ext import commands
from datetime import datetime, timedelta

class UserProfile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@bot.slash_command(name='profile', description='Показать статистику профиля')
async def profile(ctx: disnake.Interaction):
    user = ctx.author
    member = ctx.guild.get_member(user.id)

    # Кол-во дней на сервере
    now = datetime.now()
    joined_at = member.joined_at
    days_on_server = (now - joined_at).days

    # Кол-во часов в голосовых каналах
    voice_time = timedelta()
    for vc in member.voice_states:
        if vc.channel:
            voice_time += (now - vc.start_time)
    hours_in_voice_channels = round(voice_time.total_seconds() / 3600)

    # Кол-во сообщений в чатах
    message_count = 0
    async for message in ctx.channel.history(limit=None):
        if message.author == user:
            message_count += 1

    # Уровень профиля и его рейтинг
    level = 1
    rating = 100

    # Создаем Embed
    embed = disnake.Embed(title=f'Профиль пользователя {user.name}')
    embed.add_field(name='Дней на сервере', value=days_on_server, inline=False)
    embed.add_field(name='Часов в голосовых каналах', value=hours_in_voice_channels, inline=False)
    embed.add_field(name='Сообщений в чатах', value=message_count, inline=False)
    embed.add_field(name='Уровень профиля', value=level, inline=False)
    embed.add_field(name='Рейтинг профиля', value=rating, inline=False)
    await ctx.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(UserProfile(bot))