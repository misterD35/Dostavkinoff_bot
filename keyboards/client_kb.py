from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# b1 = KeyboardButton('/Режим_работы')
# b2 = KeyboardButton('/Расположение')
# b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('/Выход')
# b5 = KeyboardButton('Свяжитесь со мной', request_contact=True)
# b6 = KeyboardButton('Мой город', request_location=True)

kb_client_reply = ReplyKeyboardMarkup(resize_keyboard=True)

# kb_client_reply.add(b1).add(b2).insert(b3)
# kb_client_reply.row(b1, b2, b3).row(b5, b6).add(b4)

inl_markup_after_start = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='Наша группа', url='https://t.me/+o_S4PrDH-CxjZGYy'),
            InlineKeyboardButton(text='Наш канал', url='https://t.me/dostavkinoff')]
        ])

inl_markup_catalog_cart_FAQ = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='Каталог', callback_data='Каталог'),
            InlineKeyboardButton(text='Корзина', callback_data='Корзина'),
            InlineKeyboardButton(text='FAQ', callback_data='FAQ')]
        ])
