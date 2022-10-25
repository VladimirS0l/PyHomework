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
import red
import imp_exp
import func


# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
CHOICE, VIEW, FIND, REDACT, ADD, ADD_LN, ADD_N, ADD_NOTE, CHOICE_CON, CH_CON, CHOICE_DEL, DEL, IMPORT, EXPORT, EXIT = range(15)

print('Bot started...')

def main():
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[MessageHandler(Filters.text, me.start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
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
            CHOICE_DEL: [MessageHandler(Filters.regex('^(Удалить контакт|Главное меню)$'), me.choise_delete)],
            FIND: [MessageHandler(Filters.text, func.search_contact)],
	        # VIEW: [MessageHandler(Filters.text, func.show_all_contact)],
            
	        # IMPORT: [MessageHandler(Filters.text, imp_exp.import_dict)],
	        # EXPORT: [MessageHandler(Filters.text, imp_exp.export_dict)],
	        
      	    EXIT: [MessageHandler(Filters.text, me.cancel)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', me.cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

main()