import os
import threading
import subprocess
import time

import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from pyrogram.errors import FloodWait
import asyncio
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from upgrade import upgrade


import extras
import mediainfo
import datetime
from datetime import timedelta, date ,datetime
from datetime import date as date_
from database.date import add_date ,check_expi
from pyrogram.file_id import FileId
ADMIN = int(os.environ.get("ADMIN", 5104293442))
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)


# app
bot_token = os.environ.get("TOKEN", "5964120849:AAEWPKGrU_ofVnJZNRG22AEtqWL6G08koJA") 
api_hash = os.environ.get("HASH", "5cf3577d85fd02286535ec2296934287") 
api_id = os.environ.get("ID", "12124605")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)

# preiumum
from split import ss, temp_channel, isPremmium
if isPremmium: acc = Client("myacc", api_id=api_id, api_hash=api_hash, session_string=ss)

# optionals
auth = os.environ.get("AUTH", "1291288382,1296213694,5104293442,5201973365")
ban = os.environ.get("BAN", "")
from mdisk import iswin

# start command
@app.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	old = insert(int(message.chat.id))
	try:
	    id = message.text.split(' ')[1]
	except:
	    await message.reply_text(text =f"""
Hi {message.from_user.first_name } 👋
I'm Paid Mdisk Uploader Bot 🚀\nPermanent Thumbnail Support💯\n
Send me a Mdisk link and \nI will upload it to telegram as a file/video.\n
Please /upgrade Your Subscription
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👼 𝙳𝙴𝚅𝚂 👼", url='https://t.me/Aaajats')
           ],[
           InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/anumitultrabots'),
           InlineKeyboardButton('🍂 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url='https://t.me/anumitultrabots')
           ],[
           InlineKeyboardButton('🍃 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
           InlineKeyboardButton('ℹ️ Subscribe 🧐', url='https://youtube.com/@anumitultrabots')
           ]]
          )
       )

# upgrade command
@app.on_message(filters.private & filters.command(["upgrade"]))
async def start(client,message):
	await message.reply_text(text =f"""
	Hello \n
	🛡️ PLAN 🛡️\n
	🌸Daily  Upload  limit Unlimited\n
	🌸Price Rs 60 🇮🇳/🌎 1.5$  per Month__
	
	💸Pay Using Upi I'd \nultrabots.famc@idfcbank\n
	💸Pay Using qr code send /qr command\n
	💸After Payment Send Screenshots Of\nPayment To Admin
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Aaajats")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/ajak4406")],
		                [InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
       )

#plans command
@app.on_message(filters.private & filters.command(["plans"]))
async def start(client,message):
	await message.reply_text("""
	PAID PLANS AVAILABLE\n
	🛡️ PLAN 🛡️\n
	🌸Daily  Upload  limit Unlimited
	🌸Price Rs 40 🇮🇳/🌎 1$  per Month__
	🌸No Timeout\n
Please /upgrade your subscription
	""")
	
# qr code
@app.on_message(filters.private & filters.command(["qr"]))
async def start(client,message):
	await message.reply_photo("https://telegra.ph/file/fddcc0ebfc76cb9d05a5f.jpg"),


#total user
@app.on_message(filters.private & filters.command('total'))
async def sts(c, m):
    ids = getid()
    tot = len(ids)
    await m.reply_text(text=f"Total user(s) {tot}", quote=True)

#addpremium user

@app.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("Select Plan.........",quote=True,reply_markup=InlineKeyboardMarkup([[  
        			InlineKeyboardButton("VIP 2",callback_data = "vip2") ]]))
        			

@app.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "") 
	usertype(int(user_id),"VIP1")
	addpre(int(user_id))
	await update.message.edit("Added successfully To batch access")
	await bot.send_message(user_id,"Hey Ur Upgraded check your plan here /myplan")

# my plan

@app.on_message(filters.private & filters.command(["myplan"]))
async def start(client,message):
	used_ = find_one(message.from_user.id)	
	daily = used_["daily"]
	expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
	if expi != 0:
	     today = date_.today()
	     pattern = '%Y-%m-%d'
	     epcho = int(time.mktime(time.strptime(str(today), pattern)))
	     daily_(message.from_user.id,epcho)
	     used_limit(message.from_user.id,0)
	_newus = find_one(message.from_user.id)
	used = _newus["used_limit"]
	limit = _newus["uploadlimit"]
	remain = int(limit)- int(used)
	user =  _newus["usertype"]
	ends = _newus["prexdate"]
	if ends == None:
	    text = f"User ID:- ```{message.from_user.id}```\nPlan :- {user}\n
	else:
	    normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d')
	    text = f"User ID:- ```{message.from_user.id}```\nPlan :- {user}\nYour Plan Ends On :- {normal_date}"
	    
	if user == "Free":
	    await message.reply(text,quote = True,reply_markup = InlineKeyboardMarkup([[       			InlineKeyboardButton("Upgrade 💰💳",callback_data = "upgrade"), InlineKeyboardButton("Cancel ✖️ ",callback_data = "cancel") ]]))
	else:
	    await message.reply(text,quote=True)


