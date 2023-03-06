from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import token_Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

# storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token_Bot)
dp = Dispatcher(bot)
# dp = Dispatcher(bot, storage=storage)
