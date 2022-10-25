import logging as log
from sqlalchemy import LABEL_STYLE_TABLENAME_PLUS_COL
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import json
import menu
import check

CHOICE, VIEW, FIND, REDACT, ADD, ADD_LN, ADD_N, ADD_NOTE, CHOICE_CON, CH_CON, CHOICE_DEL, DEL, IMPORT, EXPORT, EXIT = range(15)


dict_phone = {}
search_phone = []
num_phone = 0

def name(update, _):
    global dict_phone
    if check.check_text(update, update.message.text):
        dict_phone["name"] = (update.message.text).title()
        update.message.reply_text('Введите фамилию нового контакта: ')
        return ADD_LN
    else: return ADD
    # {'name': '37475885', 'lastname': 'Сол', 'notes': 'Попвп'}
    # <class 'dict'>

def lastname(update, _):
    global dict_phone
    if check.check_text(update, update.message.text):
        dict_phone["lastname"] = (update.message.text).title()
        update.message.reply_text('Введите номер нового контакта: ')
        return ADD_N
    else: return ADD_LN

def number(update, _):
    global dict_phone
    if check.check_phone(update, update.message.text):
        dict_phone["number"] = (update.message.text).title()
        update.message.reply_text('Введите заметку о новом контакте: ')
        return ADD_NOTE
    else: return ADD_N

def notes(update, _):
    global dict_phone
    if check.check_text(update, update.message.text):
        dict_phone["notes"] = (update.message.text).title()
        read_write(dict_phone, 'rw')
        update.message.reply_text('Отлично, новый контакт успешно создан')
        return menu.start(update, _)
    else: return ADD_NOTE

def read_write(dict_phone, arg):
    
    print(dict_phone)
    if arg == "rw":
        try:
            with open('dict_bd.json', 'r') as f:
                phone_dir = json.load(f)
        except:
            phone_dir = []
        print(phone_dir)
        phone_dir.append(dict_phone)
        with open('dict_bd.json', 'w') as file:
            json.dump(phone_dir, file, indent=2, ensure_ascii = False)
        
    elif arg == "r":
        try:
            with open('dict_bd.json', 'r') as f:
                phone_dir = json.load(f)
        except:
            phone_dir = []
        return phone_dir

# def read_write_change(text, arg):
#     global num_phone
#     global search_phone
#     with open('dict_bd.json', 'r') as f:
#         phone_dir = json.load(f)
#     temp_num = phone_dir.index(search_phone[num_phone - 1])
#     phone_dir[temp_num][arg] = text
#     with open('dict_bd.json', 'w') as file:
#             json.dump(phone_dir, file, indent=2, ensure_ascii = False)

def show_all_contact(update, _):
    phone_dir = read_write(dict_phone, 'r')
    if len(phone_dir) == 0:
        update.message.reply_text("У вас пока нет контактов")
        return menu.start(update, _)
    update.message.reply_text("Найдены следующие контакты")
    for num, i in enumerate(phone_dir):
        update.message.reply_text(f' {num + 1}: ')
        update.message.reply_text(f'{i["name"]}: \n '
                                    f'{i["lastname"]}: \n'
                                    f'{i["number"]}: \n'
                                    f' {i["notes"]} \n')
    update.message.reply_text('Перевод в основное меню')
    return menu.start(update, _)

def search_contact(update, _):
    phone_dir = read_write(dict_phone, 'r')
    global search_phone
    if not (update.message.text).isnumeric():
        for i in phone_dir:
            if update.message.text in i["name"] or update.message.text in i["lastname"]:
                search_phone.append(i)
    else:
        for i in phone_dir:
            if update.message.text in i["number"]:
                search_phone.append(i)
    
    if len(search_phone) == 0:
        update.message.reply_text('Контакт в записной книге не найден')
        return menu.answer_search(update, _)
    
    update.message.reply_text(f'Найдено {len(search_phone)} контактов: ')
    for num, i in enumerate(search_phone):
        update.message.reply_text(f' {num + 1}: ')
        update.message.reply_text(f'{i["name"]}: \n '
                                    f'{i["lastname"]}: \n'
                                    f'{i["number"]}: \n'
                                    f' {i["notes"]} \n')
    
    

    reply_keyboard = [['Выбрать контакт', 'Найти контакт', 'Главное меню']]

    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(    
        'Что хотите следать с контактом?',
        reply_markup=markup_key)
    return CHOICE_CON


#CH_CON
def choise_contact(update, _):
    global search_phone
    global num_phone
    print(search_phone)
    print(type(search_phone))
    num_phone = int(update.message.text)
    
    update.message.reply_text(f'Контакт №{num_phone}: ')
    update.message.reply_text(f'Имя: {search_phone["name"]}\n'
                              f'Фамилия: {search_phone["lastname"]}\n'
                              f'Телефон: {search_phone["number"]}\n'
                              f'Заметка: {search_phone["notes"]}\n')

    reply_keyboard = [['Удалить', 'Главное меню']]

    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(    
        'Что хотите сделать с контактом?',
        reply_markup=markup_key)
    return CHOICE_DEL


def ch_del(update, _):
    global num_phone
    global search_phone
    print(search_phone)
    print(type(search_phone))
    phone_dir = read_write(dict_phone, 'r')
    phone_dir.remove(search_phone[num_phone - 1])
    search_phone = []
    with open('dict_db.json', 'w') as file:
        json.dump(phone_dir, file, indent=2, ensure_ascii = False)










