from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("All tasks", None, "all_tasks"),
        InlineKeyboardButton("Accepted tasks", None, "accepted_tasks"),
    ]
    markup.row(*buttons)
    return markup
