import logging as log
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


def check_text(update, text):
    if len(text) > 15:
        update.message.text('Введенной Вами значение слишком длинное')
        return False
    else:
        return True

def check_phone(update, text):
    if len(text) > 12:
        update.message.text('Введенной Вами значение слишком длинное')
        return False
    for i in text:
        if i.isalpha():
            update.message.text('Введенной Вами значение является текстом')
            return False
    return True

