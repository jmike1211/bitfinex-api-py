from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.dispatcher import run_async
import telegram

import requests
import time
import os
import sys
import asyncio
import functools

from bfxapi import Client

bfx = Client(
  logLevel='DEBUG',
)

token = ""
tbot = telegram.Bot(token)

def SendMessage(text):
    try:
        tbot.sendMessage("@your telegram group",text)
    except:
        tbot.sendMessage("@your telegram group",text)

async def return_frr():
    ticker = await bfx.rest.get_public_ticker('fUSD')
    print ("[FRR, BID, BID_PERIOD, BID_SIZE, ASK, ASK_PERIOD, ASK_SIZE, DAILY_CHANGE,DAILY_CHANGE_PERC, LAST_PRICE, VOLUME, HIGH, LOW, _PLACEHOLDER, _PLACEHOLDER, FRR_AMOUNT_AVAILABLE]")
    print ("Ticker:")
    print (ticker)
    mul_frr = ticker[0]*365
    high_ask = ticker[11]*365
    last_price= ticker[9]*365
    result = 'frr percent: {:.2%}({:.5f}), high ask:{:.2%}({:.5f}),last price:{:.2%}({:.5f})'.format(
        mul_frr,
        ticker[0],
        high_ask,
        ticker[11],
        last_price,
        ticker[9])
    SendMessage(result)

async def run():
    await return_frr()
"""
t = asyncio.ensure_future(run())
asyncio.get_event_loop().run_until_complete(t)
print(t)
"""
while True:
    t = asyncio.ensure_future(run())
    asyncio.get_event_loop().run_until_complete(t)

    time.sleep(900)	