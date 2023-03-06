from aiogram.types import Message
from aiogram.utils import executor
from create_bot import dp, bot
from handlers import client_views
from Dostavkinoff_bot.functions.start import when_start


@dp.message_handler()
async def echo(message: Message):
    text = f'Оу, что я вижу... Ты написал: {message.text}'
    # await bot.send_message(chat_id=message.from_user.id, text=text)   # отправить сообщение. Обязательные аргументы chat_id и text
    await message.answer(text)   # отправить сообщение в этом же чате
    # await message.reply(text)   # ответить, переслав сообщение

client_views.register_handlers_start(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=when_start)   # запуск полинга, пропускаем обновления, на старте активируем on_startup
