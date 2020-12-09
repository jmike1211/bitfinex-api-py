import time
import os
import sys
import asyncio
import functools

from bfxapi import Client
from bfxmongo import useMongo
from config import Config 
from calfundingrate import calRate

sys.path.append('bfxapi')
from models import FundingCreditModel


API_KEY = Config.config()["bfxKey"]
API_SECRET = Config.config()["bfxSec"]
bfx = Client(
    API_KEY=API_KEY,
    API_SECRET=API_SECRET,
    logLevel='INFO'
)

async def create_funding(amount, frrRate, days=2):
    print("create funding")
    response = await bfx.rest.submit_funding_offer("fUSD", amount, frrRate, days)
    # response is in the form of a Notification object
    # notify_info is in the form of a FundingOffer
    print ("Offer: ", response)

async def cancel_funding(offerid):
    response = await bfx.rest.submit_cancel_funding_offer(offerid)
    # response is in the form of a Notification object
    # notify_info is in the form of a FundingOffer
    print ("Offer: ", response.notify_info)


async def cancel_funding_all():
    response = await bfx.rest.submit_cancel_funding_offer_all("USD")
    # response is in the form of a Notification object
    # notify_info is in the form of a FundingOffer
    print ("Offer: ", response.notify_info)

async def log_wallets():
    wallets = await bfx.rest.get_wallets()
    for w in wallets:
        if w[0] == "funding" and w[1] == "USD":
            print(w[2])
            return w[2]#only catch USD balance

async def log_funding_credits():
    credits = await bfx.rest.get_funding_credits('fUSD')
    print ("Funding credits:")
    result = 0
    for c in credits:
      result =result + c[FundingCreditModel.AMOUNT] 
      print(c[FundingCreditModel.AMOUNT])
    print(result)
    return result

async def run():
    
    await cancel_funding_all()
    balance =await log_wallets()
    useamount = await log_funding_credits()

    frrRate = useMongo().mongofindone({},"frrrate")["frr"]
    amount = balance - useamount - 100
    print("balance::",balance,"amount::",amount)
    if amount < 50:
        print("balance not enough")
        return
    #if frrRate > 0.00055:
        #days = 30
        #await create_funding(amount, frrRate, days)
    #else:
        #await create_funding(amount, frrRate)
    frrRate, days = calRate.fundingRate()
    try:
        await create_funding(amount, frrRate, days)
    except:
        print("wait for moment")
while True:
    t = asyncio.ensure_future(run())
    asyncio.get_event_loop().run_until_complete(t)

    localtime = time.localtime(time.time())
    print ("local time :", localtime)
    print("start funding")
    time.sleep(900)	
