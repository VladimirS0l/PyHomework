
# import logging
import menu
import calculate as rt
import game as bt


from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

from config import TOKEN

first_question, want_play, exit_play, choose_num_can, choose_max_num, start_play, \
    create_name, step_first_pl, step_second_pl, want_count = range(10)

def cancel(update, _):
    update.message.reply_text(
        'Приходите еще',
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END

updater = Updater(TOKEN)
dispatcher = updater.dispatcher
conv_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.text, menu.start)],
    states={
        bt.first_question: [MessageHandler(Filters.regex('^Калькулятор|Игра|Выход)$'), menu.answer_fq)],
        menu.want_count: [MessageHandler(Filters.text, rt.get_rational)],

        bt.want_play: [MessageHandler(Filters.regex('^Бот|Человек)$'), bt.choose_mod)],
        bt.choose_num_can: [MessageHandler(Filters.text, bt.check_num_can)],
        bt.choose_max_can: [MessageHandler(Filters.text, bt.check_max_can)],
        bt.start_play: [MessageHandler(Filters.text, bt.main_func)],
        bt.create_name: [MessageHandler(Filters.text, bt.check_name)],
        bt.step_first_pl: [MessageHandler(Filters.text, bt.main_step_first)],
        bt.step_second_pl: [MessageHandler(Filters.text, bt.main_step_second)],

        bt.exit_play: [MessageHandler(Filters.text, cancel)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# GAME, CALCULATE = range(2)

#     # Определяем обработчик разговоров `ConversationHandler` 
#     # с состояниями GENDER, PHOTO, LOCATION и BIO
#     conv_handler = ConversationHandler( # здесь строится логика разговора
#         # точка входа в разговор
#         entry_points=[CommandHandler('start', start)],
#         # этапы разговора, каждый со своим списком обработчиков сообщений
#         states={
#             GAME: [MessageHandler(Filters.regex('^(Game|Calculate$'), game, calculate)],
#             CALCULATE: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            
#         },
#         # точка выхода из разговора
#         fallbacks=[CommandHandler('cancel', cancel)],
#     )

#     # Добавляем обработчик разговоров `conv_handler`
dispatcher.add_handler(conv_handler)

# Запуск бота
updater.start_polling()
updater.idle()