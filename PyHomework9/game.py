from glob import glob
from random import random
from matplotlib.pyplot import step
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from random import randint

first_question, want_play, exit_play, choose_num_can, choose_max_num, start_play, \
    create_name, step_first_pl, step_second_pl, want_count = range(10)

temp_list = []
list_name = []

def choose_mod(update, _):
    if update.message.text == 'Бот':
        #logger.my_log(update, CallbackContext, 'Выбрал игру с ботом')
        update.message.reply_text(
            'Вы выбрали игру с ботом!',
            reply_markup=ReplyKeyboardRemove()
        )
        return choose_num_can
    else:
        #logger.my_log(update, CallbackContext, 'Выбрал игру с человеком')
        update.message.reply_text(
            'Введи имена двух человек через пробел!',
            reply_markup=ReplyKeyboardRemove()
        )
        return create_name

def check_name(update, _):
    global list_name
    text_m = update.message.text
    try:
        name_first, name_second = text_m.split()
        if name_first == name_second:
            update.message.reply_text('Вы ввели 2 одинаковых имя!')
            name_first += '-1'
            name_second += '-2'
    except:
        update.message.reply_text('Вы ввели имена некорректно, повторите еще раз!')
        return create_name
    
    random_num = randint(0, 1)
    if random_num:
        list_name.append(name_first)
        list_name.append(name_second)
    else:
        list_name.append(name_second)
        list_name.append(name_first)

    #logger.my_log(update, CallbackContext, 'Игрок задал 2 имени {list_name[0]} и {list_name[1]}')
    update.message.reply_text(f'Отлично первым ходит {list_name[0]} ')
    return choose_num_can

def check_num_can(update, _):
    global temp_list
    temp_list = []
    try:
        num = int(update.message.text)
        if num <= 2:
            update.message.reply_text(f'Число конфет должно быть больше 2х')
            return choose_num_can
        temp_list.append(num)

        update.message.reply_text(f'Отлично, сколько конфет будете брать?')

    except:
        return check_max_can

def check_max_can(update, _):
    global temp_list
    global list_name
    try:
        num = int(update.message.text)
        if num > temp_list:
            update.message.reply_text(f'Число больше чем общее кол-во конфет')
            return choose_max_num
        if num <= 1:
            update.message.reply_text(f'Число не может быть меньше 2х')
            return choose_max_num
        if len(list_name) == 0:
            update.message.reply_text(f'Бот ходит первым')
            if temp_list[0] <= temp_list[1]:
                num_cand_first_player = temp_list[0]
                #logger.my_log(update, CallbackContext, 'Бот взял {num_cand_first_player} конфет')
            else:
                num_cand_first_player = temp_list[0] - (temp_list[1] + 1) // (temp_list[1] + 1)
                #logger.my_log(update, CallbackContext, 'Бот взял {num_cand_first_player} конфет')
            update.message.reply_text(f'Бот взял {num_cand_first_player} конфет')
            temp_list[0] -= num_cand_first_player
            update.message.reply_text(f'Осталось {temp_list[0]} конфет')
            return start_play
        else:
            update.message.reply_text(f'Отлично начинаем игру всего конфет {temp_list[0]}')
            return step_first_pl
    except:
        update.message.reply_text(f'Вы ввели некорректное число конфет')
        return choose_max_num

def main_func(update, _):
    global temp_list



