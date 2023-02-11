import telebot
import openai
import datetime
import os

accessed = False

if not os.path.exists('log_bot.txt'):
    with open('log_bot.txt', 'w') as f:
        pass

bot = telebot.TeleBot("5708223380:AAHur366QF0R-ZrIwaWSDNUsOWUAK0GYHTM")
openai.api_key = "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"


@bot.message_handler(commands=["start"])
def welcome(message):
    if message.from_user.first_name is not None:
        bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, "Helo Unknown ")


@bot.message_handler(commands=["startx"])
def welcomex(message):
    if message.from_user.first_name is not None:
        bot.send_message(message.chat.id, message.from_user.first_name + " " + " доступ разрешен")
    else:
        bot.send_message(message.chat.id, "Unknown доступ разрешен")
    global accessed
    accessed = True


@bot.message_handler(commands=["starty"])
def welcomey(message):
    if message.from_user.first_name is not None:
        bot.send_message(message.chat.id, message.from_user.first_name + " " + " доступ закрыт")
    else:
        bot.send_message(message.chat.id, "Unknown доступ закрыт")
    global accessed
    accessed = False


# @bot.message_handler(content_types=["speaks"])
# def say(message):
#    with open('log_bot.txt', 'r') as f:
#        bot.send_message(message.chat.id, f.read())


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if accessed:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{message.text}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        bot.send_message(message.chat.id, response.choices[0].text)
        if message.from_user.first_name is not None:
            with open('log_bot.txt', 'r+') as f:
                f.seek(0, 2)  # перемещение курсора в конец файла
                f.write(str(
                    datetime.datetime.now()) + " " + message.from_user.first_name + ":" + message.text + "\n")
                bot.send_message(5399791575, message.from_user.first_name + ":" + message.text)
                bot.send_message(5399791575, response.choices[0].text)
                print(str(
                    datetime.datetime.now()) + " " + message.from_user.first_name + ":" + message.text + "\n")
                f.write(str(datetime.datetime.now()) + " Answer:" + response.choices[0].text + "\n")
                print(str(datetime.datetime.now()) + " Answer:" + response.choices[0].text + "\n")


bot.polling()