import telebot

# import openai

bot = telebot.TeleBot("5809142428:AAFI2KaPp7gM0z5inOBoifKwckcUiG2pjJ4")


# openai.api_key = "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"



@bot.message_handler(content_types=["text"])
def handle_text(message):

    bot.send_message(message.chat.id, "Привет! " + message.text)


bot.polling()
