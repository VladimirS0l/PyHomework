import logging as log
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

CHOICE, CALC, GAME,SWEET, MEN, STEP, START, PL_FIRST, PL_SECOND, EXIT = range(10)

def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['CALC', 'GAME', 'EXIT']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Меня зовут профессор Бот. '
        'Команда /cancel, чтобы прекратить разговор.\n\n'
        'Поиграем или посчитаем?',
        reply_markup=markup_key,)
    return CHOICE

def first_ans(update, _):
    if update.message.text == 'EXIT':
        update.message.reply_text(f'{update.effective_user.first_name}\n'
            'Очень жаль заходи еще\n'
            'я буду рад если ты скажешь Досвидания',
            reply_markup=ReplyKeyboardRemove(),
        )
        return EXIT

    elif update.message.text == 'CALC':
        update.message.reply_text(f'{update.effective_user.first_name}\n'
            'Введи уравнение, а я её посчитаю'
            'Пример: 2*4*6-10/20',
            reply_markup=ReplyKeyboardRemove(),
        )
        return CALC

    elif update.message.text == 'GAME':
        reply_keyboard = [['BOT', 'MEN']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(f'{update.effective_user.first_name}\n'
        'Выбери режим Бот или Человек',
        reply_markup=markup_key,)
        return GAME

def calculate(update, _):
    expr = (update.message.text)
    list_number = []
    list_operation = []
    expr = expr + ' '
    temp = ''
    for i in expr:
        if i.isdigit():
            temp += i
        else:
            list_number.append(temp)
            temp = ''
    list_number = list(filter(lambda x: x != '', list_number))
    list_number = list(map(float, list_number))


    list_operation = list(filter(lambda x: x == '/' or x == '*' or x == '+' or x == '-', expr))

    while len(list_operation) > 0:
        while '/' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '/':
                    list_number[i] = list_number[i] / list_number[i+1]
                    del list_number[i+1]
                    del list_operation[i]
                    
        while '*' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '*':
                    list_number[i] = list_number[i] * list_number[i+1]
                    del list_number[i+1]
                    del list_operation[i]
                    
        while '+' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '+':
                    list_number[i] = list_number[i] + list_number[i+1]
                    del list_number[i+1]
                    del list_operation[i]
                    
        while '-' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '-':
                    list_number[i] = list_number[i] - list_number[i+1]
                    del list_number[i+1]
                    del list_operation[i]
                    
    res_list = list_number[0]
    
    update.message.reply_text(f'{update.effective_user.first_name}\n'
        f'Результат уравнения = {res_list}')

    reply_keyboard = [['CALC', 'GAME', 'EXIT']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Что хотите сделать еще?',
        reply_markup=markup_key,)
    return CHOICE


def cancel(update, _):
        # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END
    
            
    