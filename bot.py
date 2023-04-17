# import telebot
# import os

# # bot_token = os.environ.get("6245614297:AAHSK1fRtjevCo3WnsIQamGEBCX-2vAYQsA")

# bot = telebot.TeleBot("6245614297:AAHSK1fRtjevCo3WnsIQamGEBCX-2vAYQsA")

# @bot.message_handler(['start' , 'hello'])
# def send_welcome_message(message):
#     bot.reply_to(message , "Welcome to the Trial bot of Pravesh")

# @bot.message_handler(func=lambda msg:True)
# def send_to_sender(message):
#     bot.reply_to(message , message.text)

# bot.infinity_polling()

import os
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

TOKEN = "6245614297:AAHSK1fRtjevCo3WnsIQamGEBCX-2vAYQsA"
bot = telegram.Bot(token=TOKEN)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello, I'm a bot!")

def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()
