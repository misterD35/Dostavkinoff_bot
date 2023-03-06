from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Dostavkinoff_bot.config import group_chanel_id
from Dostavkinoff_bot.create_bot import bot, dp
from Dostavkinoff_bot.keyboards.client_kb import inl_markup_after_start, inl_markup_catalog_cart_FAQ


async def check_subscribe(message: types.Message):
    subscriber = 0
    for chat_id in group_chanel_id:
        sub = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
        if sub.status != types.ChatMemberStatus.LEFT:
            subscriber += 1
        else:
            break
    if subscriber == len(group_chanel_id):
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text="Привет! Рады, что ты с нами!\nТеперь ты можешь сделать свой первый заказ",
                                  reply_markup=inl_markup_catalog_cart_FAQ)
    else:
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text='Привет! \nДля того, чтобы начать, подпишись на нашу группу и канал, затем повтори попытку, нажав /start',
                                  reply_markup=inl_markup_after_start)
        raise CancelHandler()
