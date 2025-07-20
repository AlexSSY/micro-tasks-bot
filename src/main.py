import telebot

import settings


bot = telebot.TeleBot(token=settings.BOT_TOKEN)


@bot.message_handler(["start"])
def start_handler(message):
    bot.reply_to(message, "Howdy, how are you doing?")


bot.infinity_polling()
