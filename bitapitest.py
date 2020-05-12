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
from bfxmongo import useMongo
from config import Config

token = Config.config()["apiBottoken"]
updater = Updater(token, use_context=True)

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
    if len(update.message.text[7:]) != 43:
        context.bot.send_message(chat_id=update.effective_chat.id, text="length wrong")
        return 
    if ("addkey:" in update.message.text):
        API_KEY= update.message.text[7:]
        mongoResult = {"user_id":update.message.from_user.id,"API_KEY":update.message.text[7:]}
        useMongo().mongoupsertone({"user_id":update.message.from_user.id},mongoResult)
        result = "your key is :" + API_KEY[0:4] + " ... " + API_KEY[-4:]
        context.bot.deleteMessage(chat_id=update.effective_chat.id,message_id=update.message.message_id)
    elif ("addsec:" in update.message.text):
        API_SEC= update.message.text[7:]
        mongoResult = {"user_id":update.message.from_user.id,"API_SEC":update.message.text[7:]}
        useMongo().mongoupsertone({"user_id":update.message.from_user.id},mongoResult)
        result = "your sec is :" + API_SEC[0:4] + " ... " + API_SEC[-4:]
        context.bot.deleteMessage(chat_id=update.effective_chat.id,message_id=update.message.message_id) 
    else:
        result = "no rule"
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

updater.dispatcher.add_handler(CommandHandler('meInfo', getYourInformation))

updater.start_polling()
