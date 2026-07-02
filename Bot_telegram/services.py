import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def load_questions(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def make_inline_keyboard(items, prefix):
    keyboard = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(
            text=item,
            callback_data=f"{prefix}:{item}"
        )
        for item in items
    ]

    keyboard.add(*buttons)

    return keyboard