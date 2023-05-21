# bot.py
import telebot
from config import TOKEN

# Bot initialization
bot = telebot.TeleBot(TOKEN)

# Bot logic goes here...

# Start the bot
bot.polling()
