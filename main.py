import os
import time
import requests
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
API_URL = "https://topsmm.com/api/v2"

bot = telebot.TeleBot(BOT_TOKEN)
bot.remove_webhook()
time.sleep(1)

def api_request(action, **params):
    params.update({"key": API_KEY, "action": action})
    try:
        r = requests.post(API_URL, data=params, timeout=30)
        return r.json()
    except:
        return {"error": "API қате"}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("1. Қызмет тапсырыс беру", "2. Баланс")
    markup.add("3. Менің тапсырыстарым")
    bot.send_message(message.chat.id, "Сәлеметсіз бе! 👋\nSMM қызметтеріне қош келдіңіз", reply_markup=markup)

print("Bot is running...")
bot.polling(none_stop=True)
