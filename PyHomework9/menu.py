# import logger
from venv import create
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

first_question, want_play, exit_play, choose_num_can, choose_max_num, start_play, \
    create_name, step_first_pl, step_second_pl, want_count = range(10)
temp_list = []
list_name = []

def start(update, _):
    #logger.my_log(update, CallbackContext, 'Зашел в программу')
    reply_keyboard = [['Калькулятор', 'Игра', 'Выход']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        f'Привет {update.effective_user.first_name}!\n'
        'В этом боте ты можешь:\n'
        '1) Воспользоваться калькулятором\n'
        '2) Сыграть в игру\n'
        '3) Завершить программу\n'
        '/cancel',
        reply_markup = markup_key,)
    return first_question

def answer_fq(update, _):
    if update.message.text == 'Выход':
        #logger.my_log(update, CallbackContext, 'Ни чего не захотел делать')
        update.message.reply_text(
        'Заходите еще!',
        reply_markup=ReplyKeyboardRemove()
        )
        return exit_play

    elif update.message.text == 'Калькулятор':
        logger.my_log(update, CallbackContext, 'Зашел в калькулятор')
        update.message.reply_text(
            f'{update.effective_user.first_name}\n'
            'Введите выражение, которое хотите посчитать'),
        return want_count

    elif update.message.text == 'Игра':
        #logger.my_log(update, CallbackContext, 'Зашел в игру')
        reply_keyboard = [['Бот', 'Человек']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(
            f'{update.effective_user.first_name}\n'
            'Введите выражение, которое хотите посчитать',
            reply_markup = markup_key,)
        return want_count

        
