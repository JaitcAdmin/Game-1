import telebot
import os

bot = telebot.TeleBot("6070646823:AAHzI_ydOBKoodYn1602hOywN2dU0eMYk1M")


@bot.message_handler(commands=["update"])
def update():
    os.system("OpenAI.py")
    print("f")

bot.polling()