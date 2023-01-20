import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import asyncio
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from upgrade import upgrade


from config import BATCH_ACCESS


import datetime
from datetime import timedelta, date ,datetime
from datetime import date as date_
from database.date import add_date ,check_expi
from pyrogram.file_id import FileId
ADMIN = int(os.environ.get("ADMIN", 1883570185))
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)


# app
bot_token = os.environ.get("TOKEN", "5964120849:AAEWPKGrU_ofVnJZNRG22AEtqWL6G08koJA") 
api_hash = os.environ.get("HASH", "5cf3577d85fd02286535ec2296934287") 
api_id = os.environ.get("ID", "12124605")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)

# upgrade command
@client.on_message(filters.private & filters.command(["upgrade"]))
async def start(client,message):
	await message.reply_text(text =f"""
	Hello \n
	🛡️ PLAN 🛡️\n
	🌸Daily  Upload  limit Unlimited\n
	🌸Price Rs 150 🇮🇳/🌎 1.85$  per Month__
	
	💸Pay Using Upi I'd \njaswindersingh42794@oksbi\n
	💸Pay Using qr code send /qr command\n
	💸After Payment Send Screenshots Of\nPayment To Admin
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Cyniteofficial")], 
        			[InlineKeyboardButton("Paytm 🌎",url = "https://t.me/Cyniteofficial")],
		                [InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
       )

#plans command
@app.on_message(filters.private & filters.command(["plans"]))
async def start(client,message):
	await message.reply_text("""
	PAID PLANS AVAILABLE\n
	🛡️ PLAN 🛡️\n
	🌸Price Rs 150 🇮🇳/🌎 1.85$  per Month__
	🌸No Timeout\n
Please /upgrade your subscription
	""")
	
# qr code
@app.on_message(filters.private & filters.command(["qr"]))
async def start(client,message):
	await message.reply_photo("https://telegra.ph/file/f38072c0768fe42f93e77.jpg"),

#addpremium user

@app.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("Select Plan.........",quote=True,reply_markup=InlineKeyboardMarkup([[  
        			InlineKeyboardButton("VIP",callback_data = "vip1") ]]))
        			

@app.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "") 
	usertype(int(user_id),"VIP1")
	addpre(int(user_id))
	await update.message.edit("Added successfully To batch access")
	await bot.send_message(user_id,"Hey Ur Upgraded check your plan here /myplan")
