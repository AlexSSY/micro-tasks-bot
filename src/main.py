import telebot

import settings
import keyboards


bot = telebot.TeleBot(token=settings.BOT_TOKEN)


@bot.message_handler(["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Pick", reply_markup=keyboards.main_menu_keyboard())


def all_handler(message):
    bot.reply_to(message, "All messages handler.")
bot.register_message_handler(all_handler, func=lambda _: True)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "all_tasks":
        bot.edit_message_text("Picked All Tasks", call.message.chat.id, call.message.id, reply_markup=keyboards.main_menu_keyboard())
    elif call.data == "accepted_tasks":
        bot.edit_message_text("Picked Accepted Tasks", call.message.chat.id, call.message.id, reply_markup=keyboards.main_menu_keyboard())


bot.infinity_polling()
