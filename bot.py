import telebot
import os

# bot_token = os.environ.get("6245614297:AAHSK1fRtjevCo3WnsIQamGEBCX-2vAYQsA")

bot = telebot.TeleBot("6245614297:AAHSK1fRtjevCo3WnsIQamGEBCX-2vAYQsA")

@bot.message_handler(['start' , 'hello'])
def send_welcome_message(message):
    bot.reply_to(message , "Welcome to the Trial bot of Pravesh")

@bot.message_handler(func=lambda msg:True)
def send_to_sender(message):
    bot.reply_to(message , message.from_user.username)
    bot.reply_to(message , message.text)

bot.infinity_polling()

