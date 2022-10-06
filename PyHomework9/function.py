import logging


from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

GAME, CALCULATE = range(2)

def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['Game', 'Calculate']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Бот предлагает Вам на выбор поиграть с ним в игру или посчитать',
        reply_markup=markup_key,)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    return GAME or CALCULATE
    

def game(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info("Пол %s: %s", user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    update.message.reply_text(
        'Хорошо. Пришли мне свою фотографию, чтоб я знал как ты '
        'выглядишь, или отправь /skip, если стесняешься.',
        #reply_markup=ReplyKeyboardRemove(),
    )
    # переходим к этапу `PHOTO`
    return ConversationHandler.END

def calculate(update, _):
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info("Пол %s: %s", user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    update.message.reply_text(
        'Хорошо. Пришли мне свою фотографию, чтоб я знал как ты '
        'выглядишь, или отправь /skip, если стесняешься.'
        #reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END

def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END