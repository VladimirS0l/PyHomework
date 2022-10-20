import logging as log
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import random

CHOICE, CALC, GAME,SWEET, MEN, STEP, START, PL_FIRST, PL_SECOND, EXIT = range(10)

players = []
list_sweet = []

def game(update, _):
    if update.message.text == 'BOT':
        update.message.reply_text(
            f'{update.effective_user.first_name}\n'
            'Вы выбрали игру с ботом\n'
            'Правила игры: кто возьмет последнюю\n конфету, тот и выйграл\n'
            'Напишите сколько всего будет конфет:\n ',
            reply_markup=ReplyKeyboardRemove()
            ),
        return SWEET

    elif update.message.text == 'MEN':
        update.message.reply_text(
            f'{update.effective_user.first_name}\n'
            'Вы выбрали игру с человеком\n'
            'Напишите имя второго игрока',
            reply_markup=ReplyKeyboardRemove()
            ),
        return MEN

#MEN
def player_name(update, _):
    global players
    player1 = update.effective_user.first_name
    player2 = update.message.text
    players = [player1, player2]
    random.shuffle(players)
    player1, player2 = players
    update.message.reply_text(
            f'{players[0]} будет ходить первый\n'
            f'{players[1]} будет ходить второй\n'
            'Правила игры: кто возьмет последнюю\n конфету, тот и выйграл\n'
            'Укажите сколько всего будет конфет на столе:\n '
    )
    return SWEET

#SWEET
def choose_num_sweet(update, _):
    global list_sweet
    players
    try:
        num = int(update.message.text)
        if num <= 2:
            update.message.reply_text(f'Число конфет должно быть больше 2х')
            return SWEET

        list_sweet.append(num)

        update.message.reply_text(f'Отлично, сколько конфет будете брать?\n'
                                    'Но не более 20% от общего числа')
        return STEP
    except:
        return SWEET

#STEP
def one_step(update, _):
    global list_sweet
    global players
    try:
        num = int(update.message.text)
        if num > list_sweet[0]:
            update.message.reply_text(f'Число больше чем общее кол-во конфет')
            return STEP

        if num <= 1:
            update.message.reply_text(f'Число не может быть меньше 2')
            return STEP
        
        if num > list_sweet[0] * 0.21:
            update.message.reply_text(f'Число больше 20% от общего числа конфет')
            return STEP

        list_sweet.append(num)
        if len(players) == 0:
            update.message.reply_text(f'Бот ходит первым')
            if list_sweet[0] < list_sweet[1] + 2:
                one_step_player1 = list_sweet[0] - 1
                
            else:
                one_step_player1 = list_sweet[0] - (list_sweet[1] + 2) * (list_sweet[0] // (list_sweet[1] + 2))
                
            update.message.reply_text(f'Бот взял {one_step_player1} конфет')
            list_sweet[0] -= one_step_player1
            update.message.reply_text(f'Осталось {list_sweet[0]} конфет')

            return START

        else:
            update.message.reply_text(f'Отлично начинаем игру всего конфет {list_sweet[0]}')
            return PL_FIRST
    except:
        update.message.reply_text(f'Вы ввели некорректное число конфет')
        return STEP

#START
def start_play(update, _):
    global list_sweet
    try:
        num = int(update.message.text)
        if num > list_sweet[1]:
            update.message.reply_text(f'Выбранное число конфет больше, чем можно взять')
            return START
        if num < 1:
            update.message.reply_text(f'Число конфет должно быть больше 1ой')
            return START
        if list_sweet[0] - num < 0:
            update.message.reply_text(f'Число конфет должно больше чем на столе')
            return START
    
    except ValueError:
        update.message.reply_text(f'Вы ввели неверное число попробуйте еще раз')
        return START
    
    if list_sweet[0] - num <= list_sweet[1]:
        list_sweet[0] -= num
        update.message.reply_text(f'Конфет осталось {list_sweet[0]}')
        update.message.reply_text(f'Бот выйграл')
        
        list_sweet = []
        
        reply_keyboard = [['CALC', 'GAME', 'EXIT']]
        # Создаем простую клавиатуру для ответа
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        # Начинаем разговор с вопроса
        update.message.reply_text(
            'Что хотите сделать еще?',
        reply_markup=markup_key,)
        return CHOICE

    else:
        list_sweet[0] -= num
        update.message.reply_text(f'{update.effective_user.first_name} взял {num} конфет, осталось {list_sweet[0]}\n')
        one_step_player1 = list_sweet[0] - (list_sweet[1] + 1) * (list_sweet[0] // (list_sweet[1] + 1))
        list_sweet[0] -= one_step_player1
        
        update.message.reply_text(f'Бот взял {one_step_player1} конфет, осталось {list_sweet[0]},\n'
                                    f'можно взять {list_sweet[1]}\nсколько возьмете?')
        return START

#PL_FIRST
def step_first(update, _):
    global list_sweet
    global players
    try:
        num = int(update.message.text)
        if num > list_sweet[1]:
            update.message.reply_text(f'Выбранное число конфет больше, чем можно взять')
            return PL_FIRST
        if num < 1:
            update.message.reply_text(f'Число конфет должно быть больше 1ой')
            return PL_FIRST
        if list_sweet[0] - num < 0:
            update.message.reply_text(f'Число конфет больше чем на столе')
            return PL_FIRST
        
    except:
        update.message.reply_text(f'Вы ввели неверное число попробуйте еще раз')
        return PL_FIRST
    
    if list_sweet[0] - num == 0:
        update.message.reply_text(f'Игрок {players[0]} забрал последние конфеты, '
                                    'и выйграл')
        list_sweet = []
        players = []

        reply_keyboard = [['CALC', 'GAME', 'EXIT']]
        # Создаем простую клавиатуру для ответа
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        # Начинаем разговор с вопроса
        update.message.reply_text(
            'Что хотите сделать еще?',
        reply_markup=markup_key,)
        return CHOICE
    
    list_sweet[0] -= num
    update.message.reply_text(f'{players[0]} взял {num} конфет')
    update.message.reply_text(f'{list_sweet[0]} осталось конфет, \n'
                                f'можно взять {list_sweet[1]} конфет\n'
                                f'{players[1]} сколько вы возьмете?')

    return PL_SECOND

#PL_SECOND
def step_second(update, _):
    global list_sweet
    global players
    try:
        num = int(update.message.text)
        if num > list_sweet[1]:
            update.message.reply_text(f'Выбранное число конфет больше, чем можно взять')
            return PL_FIRST
        if num < 1:
            update.message.reply_text(f'Число конфет должно быть больше 1ой')
            return PL_FIRST
        if list_sweet[0] - num < 0:
            update.message.reply_text(f'Число конфет больше чем на столе')
            return PL_FIRST
        
    except:
        update.message.reply_text(f'Вы ввели неверное число попробуйте еще раз')
        return PL_FIRST
    
    if list_sweet[0] - num == 0:
        update.message.reply_text(f'Игрок {players[1]} забрал последние конфеты, '
                                    'и выйграл')
        list_sweet = []
        players = []

        reply_keyboard = [['CALC', 'GAME', 'EXIT']]
        # Создаем простую клавиатуру для ответа
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        # Начинаем разговор с вопроса
        update.message.reply_text(
            'Что хотите сделать еще?',
        reply_markup=markup_key,)
        return CHOICE
    
    list_sweet[0] -= num
    update.message.reply_text(f'{players[1]} взял {num} конфет')
    update.message.reply_text(f'{list_sweet[0]} осталось конфет, \n'
                                f'можно взять {list_sweet[1]} конфет\n'
                                f'{players[0]} сколько вы возьмете?')

    return PL_FIRST

        

        



