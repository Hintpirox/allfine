from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**VIP **
	Price 150 🇮🇳/🌎 1.85$  per Month
		
	Pay Using Upi I'd ```jaswindersingh42794@oksbi```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/cyniteofficial")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/cyniteofficial")],
		                [InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
