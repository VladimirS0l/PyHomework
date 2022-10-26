import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import menu as me
import func


CHOICE, FIND, ADD, ADD_LN, ADD_N, ADD_NOTE, CHOICE_CON, CH_CON, CHOICE_DEL, EXIT = range(10)

print('Bot started...')

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler( 
        entry_points=[MessageHandler(Filters.text, me.start)],
        states={
            CHOICE: [MessageHandler(Filters.regex('^(Записать контакт|Найти контакт|'
                                                    'Показать контакты|Импорт БД|'
                                                    'Экспорт БД|Выйти)$'), me.first_move, func.show_all_contact)],

            ADD: [MessageHandler(Filters.text, func.name)],
            ADD_LN: [MessageHandler(Filters.text, func.lastname)],
            ADD_N: [MessageHandler(Filters.text, func.number)],
            ADD_NOTE: [MessageHandler(Filters.text, func.notes)],
            CHOICE_CON: [MessageHandler(Filters.regex('^(Выбрать контакт|Найти контакт| Главное меню)$'), me.ch_contact)],
            CH_CON:[MessageHandler(Filters.text, func.choise_contact)],
            CHOICE_DEL: [MessageHandler(Filters.regex('^(Удалить|Главное меню)$'), me.choise_delete)],
            FIND: [MessageHandler(Filters.text, func.search_contact)],
      	    EXIT: [MessageHandler(Filters.text, me.cancel)]
        },
        fallbacks=[CommandHandler('cancel', me.cancel)],
    )

    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

main()