from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async
import telegram

import requests
import time
import os
import sys
import asyncio
import functools

from bfxapi import Client

token = ""
updater = Updater(token, use_context=True)

API_KEY=""
API_SECRET=""

@run_async
async def create_funding():

    API_KEY=""
    API_SECRET=""
    print(API_KEY)
    bfx = Client(
      API_KEY=API_KEY,
      API_SECRET=API_SECRET,
      logLevel='INFO'
    )
    print("222") 
    response = await bfx.rest.submit_funding_offer("fUSD", 100, 0.0005, 2)
    # response is in the form of a Notification object
    # notify_info is in the form of a FundingOffer
    print ("Offer: ", response)


def getYourInformation(update,context):
    #update.message.reply_text('發送人 first name, {}'.format(update.message.from_user.first_name))
    #update.message.reply_text('發送人 last name, {}'.format(update.message.from_user.last_name))
    #update.message.reply_text('發送人 full name:, {}'.format(update.message.from_user.full_name))
    update.message.reply_text('發送人 username:, {}'.format(update.message.from_user.username))
    update.message.reply_text('發送人 id:, {}'.format(update.message.from_user.id))
    #update.message.reply_text('message_id:, {}'.format(update.message.message_id))
    #update.message.reply_text('所在的聊天室 id:, {}'.format(update.message.chat.id))
    #update.message.reply_text('所在的聊天室 type:, {}'.format(update.message.chat.type))
    update.message.reply_text('訊息內容:, {}'.format(update.message.text))


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    if ("addkey:" in update.message.text):
        API_KEY= update.message.text[7:]
        result = "your key is :" + API_KEY[0:4] + " ... " + API_KEY[-4:]
        context.bot.deleteMessage(chat_id=update.effective_chat.id,message_id=update.message.message_id)
    elif ("addsec:" in update.message.text):
        result = update.message.text[7:]          
    else:
        result = "no rule"
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
# 套用 getYourInformation()，當你對你的機器人說 '/meInfo'，就會執行這串
updater.dispatcher.add_handler(CommandHandler('meInfo', getYourInformation))

# 這串是執行機器人算是一個運行server?很類似 我是這樣覺得
updater.start_polling()
