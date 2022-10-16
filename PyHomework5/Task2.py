# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

print('\t\tПРИВЕТ - ЭТА ИГРА КТО ВЫТЯНЕТ ПОСЛЕДНЮЮ КОНФЕТУ')
print('Игрок 1')


def check_name_run():
    while True:
        name = input('Введите ваше имя: ')
        if name.isalpha():
            return name
        else:
            print('Вы ввели цифры')


name1 = check_name_run()


def check_sweet():
    while True:
        sweet = input('Введите максимальное количество конфет: ')
        if sweet.isdigit():
            s = int(sweet)
            if 30 < s <= 1000:
                return s
        else:
            print('Некорректный ввод')


sweet = check_sweet()


def check_onestep():
    while True:
        onestep = input(
            'Введите максимальное количество конфет, которые будем брать за один шаг: ')
        if onestep.isdigit():
            os = int(onestep)
            if 0 < os <= (sweet * 0.4):
                return os
        else:
            print('Некорректный ввод')


one_step = check_onestep()


def player_step_check():
    while True:
        player_step = input(
            f'Сколько конфет вы ходите взять, можно взять от 1 до {one_step}: ')
        if player_step.isdigit():
            ps = int(player_step)
            if 0 < ps <= one_step:
                return ps
        else:
            print('Некорректный ввод')


# Выбор режима игры (проверка на ввод режима игры)

print('Очень хорошо, теперь выбери режим игры, \n1 - игра с ботом, \n2 - игра с человеком, \n3 - выход')


def check_choose():
    while True:
        choose = input('Введите номер режима: ')
        if choose.isdigit():
            ch = int(choose)
            if 0 < ch < 4:
                return ch
        else:
            print('Некорректный ввод')


choose = check_choose()


if choose == 1:
    print('Вы выбрали режим игры с ботом')
    player1 = name1
    player2 = 'Бот'
    players = [player1, player2]
    random.shuffle(players)
    player1, player2 = players
    if player1 == 'Бот':
        while sweet > 0:
            if sweet < one_step+2:
                player1_step = sweet - 1
            else:
                player1_step = sweet - (one_step + 2) * (sweet//(one_step + 2))
            sweet -= player1_step
            print(f'{player1} взял {player1_step} конфет, всего осталось {sweet}')
            if sweet <= 0:
                print(f'{player2} выйграл')
                break
            player2_step = player_step_check()
            sweet -= player2_step
            print(f"{player2} взял {player2_step} конфет, всего осталось {sweet}")
            if sweet <= 0:
                print(f'{player1} выйграл')
                break
    else:
        while sweet > 0:
            player1_step = player_step_check()
            sweet -= player1_step
            print(f"{player1} взял {player1_step} конфет, всего осталось {sweet}")
            if sweet <= 0:
                print(f'{player2} выйграл')
                break
            if sweet < one_step+2:
                player2_step = sweet - 1
            else:
                player2_step = sweet - (one_step + 2) * (sweet//(one_step + 2))

            sweet -= player2_step
            print(f'{player2} взял {player2_step} конфет, всего осталось {sweet}')
            if sweet <= 0:
                print(f'{player1} выйграл')
                break

elif choose == 2:
    print('Вы выбрали режим игры с другим игроком, пожалуйста введите имя игрока 2')
    name2 = check_name_run()
    if name1 == name2:
        name2 += '-2'
    player1 = name1
    player2 = name2
    players = [player1, player2]
    random.shuffle(players)
    player1, player2 = players
    if player1 == name1:
        while sweet > 0:
            player1_step = player_step_check()
            sweet -= player1_step
            print(f"{player1} взял {player1_step} конфет, всего осталось {sweet}")
            if sweet <= 0:
                print(f'{player2} выйграл')
                break
            player2_step = player_step_check()
            sweet -= player2_step
            print(f"{player2} взял {player2_step} конфет, всего осталось {sweet}")
            if sweet <= 0:
                print(f'{player1} выйграл')
                break
    else:
        while sweet > 0:
            player2_step = player_step_check()
            sweet -= player2_step
            print(f"{player2} взял {player2_step} конфет, всего осталось {sweet}")
            if sweet <= 0:
                print(f'{player1} выйграл')
                break
            player1_step = player_step_check()
            sweet -= player1_step
            print(f"{player1} взял {player1_step} конфет, всего осталось {sweet}")
            if sweet <= 0:
                print(f'{player2} выйграл')
                break

elif choose == 3:
    print('Очень жаль, что не поиграл. Пока')
    input('\n\nНажмите Enter, чтобы выйти.')