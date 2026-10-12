
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🛒 خرید VPN", callback_data="buy"))
    keyboard.add(InlineKeyboardButton("💰 تعرفه‌ها", callback_data="prices"))
    keyboard.add(InlineKeyboardButton("💬 پشتیبانی", callback_data="support"))
    bot.send_message(message.chat.id, "سلام! به فروشگاه VPN خوش آمدی.", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "buy":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "برای خرید با پشتیبانی تماس بگیر.")
    elif call.data == "prices":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "تعرفه‌ها به‌زودی اعلام می‌شوند.")
    elif call.data == "support":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "پشتیبانی به‌زودی فعال می‌شود.")

bot.infinity_polling()
