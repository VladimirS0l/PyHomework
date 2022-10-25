import logging as log
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import func
import menu
import csv
import json

CHOICE, VIEW, FIND, REDACT, ADD, ADD_LN, ADD_N, ADD_NOTE, REMOVE, MOVE, IMPORT, EXPORT, EXIT = range(13)

dict_phone = {}
search_phone = []
num_phone = 0


#EXPORT
def export_dict(update, _):
    phone_dir = func.read_write(dict_phone, 'r')
    if len(phone_dir) == 0:
        update.message.reply_text('У ваc нет контактов для экспорта')
        return menu.start(update, _)
    count = 0
    with open("bd_export.csv", mode="w", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimetr = ",", lineterminator="\r")
        file_writer.writerow(["Имя\t", "Фамилия\t", "Телефон\t","Заметка\t"])
        for i in phone_dir:
            file_writer.writerow([i["name"], i["lastname"], i["number"], i["notes"]])
            count += 1
    
    update.message.reply_text(f'Экспорт бд завершен. Экспортировано {count} контактов')
    return menu.start(update, _)

def import_dict(update, _):
    result = []
    with open("bd_export.csv", mode="w", encoding='utf-8') as f:
        f = csv.reader(f, delimiter=",")
        try:
            count = 0
            for row in f:
                if count == 0:
                    count += 1
                    continue
                else:
                    temp = {}
                    temp["name"] = row[0]
                    temp["lastname"] = row[1]
                    temp["number"] = row[2]
                    temp["notes"] = row[3]
                    result.append(temp)
                count += 1
        except:
           update.message.reply_text('Импорт невозможен. Файл не соответствует стандарту')
           return menu.start(update, _)
    if len(result) == 0:
        update.message.reply_text('Файл пустой для импорта')
        return menu.start(update, _)
    count -= 1
    with open("dict_bd.json", 'w') as file:
        json.dump(result, file, indent=2, ensure_ascii=False)

    update.message.reply_text('Импорт контактов успешно завершен'
                                f'импортировано {count} контактов')
    
    return menu.start(update, _)
