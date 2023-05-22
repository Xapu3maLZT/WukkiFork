# WukkiBot

Это Discord-бот для проекта «Hodwini», на библиотеке [DisnakeAPI](https://disnake.dev/).
<br>Система модерации, уровней, экономике, синхронизация веб-сайта и Minecraft-сервера, и многое другое.

___
## Структура бота

```
Wukki/
├── cogs/
│   ├── admin/
│   │   ├── admin_broadcast.py
│   │   ├── admin_moderation.py
│   │   └── admin_utils.py
│   ├── ecosystem/
│   │   ├── telegram_synch.py
│   │   └── website_synch.py
│   ├── user/
│   │   └── profile.py
│   ├── utils/
│   │   ├── bot_profile.py
│   │   └── voice_system.py
│   └── __init.py__
├── .gitignore
├── main.py
├── config.json
└── README.md
```
___
## Команды

- `/help` - выводит список доступных команд.
- `/profile` - отображает информацию о вашем профиле.
- `/status` - отображает статус Minecraft-сервера.
- `/sell` - открывает модальное окно, для продажи предмета.
- `/balance` - отображает баланс.
- `/auth` - синхронизирует Minecraft-аккаунт с Discord-сервером.
- `/broadcast` - откроет модальное окно, для создания объявления.

> И ещё несколько других команд, весь список можно получить введя команду `/help`.
___

## Установка и запуск

Для того, чтобы установить этого бота, вам нужно клонировать проект:

 <br>```git clone https://github.com/Hodwini/WukkiBot.git```