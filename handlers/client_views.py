from Dostavkinoff_bot.create_bot import dp
from aiogram import types, Dispatcher
from Dostavkinoff_bot.functions.check_subscribe import check_subscribe


@dp.message_handler(commands=['id'])
async def id(message):
    chat_id = message.chat.id
    print(chat_id)

async def send_welcome(message: types.Message):
    await check_subscribe(message)


# async def FAQ_callback(callback_query: types.CallbackQuery):
#     await sqlite_db.sql_delete_position(callback_query.data.replace('del ', ''))
#     await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)




def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    # dp.register_callback_query_handler(delete_from_db_by_callback, lambda x: x.data and x.data.startswith('del '))
    # dp.register_message_handler(start_load_position_menu, commands=['Загрузить'], state=None)
    # dp.register_message_handler(cancel_handler, state="*", commands='Отмена')
