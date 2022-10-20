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
import game as g

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
CHOICE, CALC, GAME,SWEET, MEN, STEP, START, PL_FIRST, PL_SECOND, EXIT = range(10)

print('Bot started...')

def main():
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[MessageHandler(Filters.text, me.start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOICE: [MessageHandler(Filters.regex('^(CALC|GAME|Other)$'), me.first_ans)],
            CALC: [MessageHandler(Filters.text, me.calculate)],

            GAME: [MessageHandler(Filters.regex('^(BOT|MEN)$'), g.game)],
            SWEET: [MessageHandler(Filters.text, g.choose_num_sweet)],
            STEP: [MessageHandler(Filters.text, g.one_step)],
            START: [MessageHandler(Filters.text, g.start_play)],
            MEN: [MessageHandler(Filters.text, g.player_name)],
            PL_FIRST: [MessageHandler(Filters.text, g.step_first)],
            PL_SECOND: [MessageHandler(Filters.text, g.step_second)],
            
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