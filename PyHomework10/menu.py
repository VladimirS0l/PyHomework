import logging as log
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import json

import  imp_exp as ie
import func


CHOICE, VIEW, FIND, REDACT, ADD, ADD_LN, ADD_N, ADD_NOTE, CHOICE_CON, CH_CON, CHOICE_DEL, DEL, IMPORT, EXPORT, EXIT = range(15)

dict_phone = {}
search_phone = []
num_phone = 0

def start(update, _):
    reply_keyboard = [['Записать контакт', 'Найти контакт', 'Показать контакты'], ['Импорт БД', 'Экспорт БД', 'Выход']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(    
        'Команда /cancel, закрыть книгу.\n\n'
        'Выберите действие',
        reply_markup=markup_key,)
    return CHOICE

#CHOICE
def first_move(update, _):
    if update.message.text == 'Выход':
        update.message.reply_text(f'{update.effective_user.first_name}\n'
            'Очень жаль заходи еще\n',
            reply_markup=ReplyKeyboardRemove(),
        )
        return EXIT

    elif update.message.text == 'Показать контакты':
        update.message.reply_text(f'{update.effective_user.first_name}\n'
            'Вывожу Вам всю записную книгу',
            reply_markup=ReplyKeyboardRemove(),
        )
        return func.show_all_contact(update, _)

    elif update.message.text == 'Найти контакт':
        update.message.reply_text(f'{update.effective_user.first_name}\n'
            'Введите первые буквы или цифры нужного контакта: ',
            reply_markup=ReplyKeyboardRemove(),
        )
        return FIND

    elif update.message.text == 'Записать контакт':
        update.message.reply_text(f'{update.effective_user.first_name}\n'
            'Введите имя нового контакта: ',
            reply_markup=ReplyKeyboardRemove(),
        )
        return ADD

    elif update.message.text == 'Импорт БД':
        return ie.import_dict(update, _)

    elif update.message.text == 'Экспорт БД':
        return ie.export_dict(update, _)

#CHOICE_CON
def ch_contact(update, _):
    if update.message.text == 'Главное меню':
        update.message.reply_text('Главное меню\n',
            reply_markup=ReplyKeyboardRemove(),
        )
        return start(update, _)
    
    elif update.message.text == 'Найти контакт':
        update.message.reply_text(f'{update.effective_user.first_name}\n'
            'Начните вводить имя, фамилию, или номер телефона: ',
            reply_markup=ReplyKeyboardRemove(),
        )
        return FIND

    elif update.message.text == 'Выбрать контакт':
        update.message.reply_text(f'{update.effective_user.first_name}\n'
            'Введите цифру контакта: ',
            reply_markup=ReplyKeyboardRemove(),
        )
        return CH_CON

def choise_delete(update, _):
    if update.message.text == 'Главное меню':
        update.message.reply_text('Главное меню\n',
            reply_markup=ReplyKeyboardRemove(),
        )
        return start(update, _)

    elif update.message.text == 'Удалить контакт':
        func.ch_del(update, _)
        update.message.reply_text('Контакт успешно удален')
        return func.ch_del(update, _)


#EXIT
def cancel(update, _):
    user = update.message.from_user
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
    
            
    