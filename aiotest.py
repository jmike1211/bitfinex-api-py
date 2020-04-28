from aiogram import Bot, Dispatcher, executor, types

import requests
import time
import os
import sys

from bfxapi import Client

API_TOKEN = ""
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

API_KEY=""
API_SECRET=""

@dp.message_handler(commands=['createfunding'])
async def create_funding(message: types.Message):

    bfx = Client(
      API_KEY=API_KEY,
      API_SECRET=API_SECRET,
      logLevel='INFO'
    )
    try:
        response = await bfx.rest.submit_funding_offer("fUSD", 100, 0.00042, 3)
    except Exception as Argument:
        response = Argument
    print ("Offer: ", response)
    await message.reply(response)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("hi this is boti")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
