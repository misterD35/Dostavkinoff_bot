from Dostavkinoff_bot.create_bot import dp, bot
from Dostavkinoff_bot.data_base import sqlite_db
from Dostavkinoff_bot.config import user_ID


async def when_start(dp):
    await bot.send_message(chat_id=user_ID, text='Бот запущен')
    print('Бот запущен')
    sqlite_db.sql_start()
