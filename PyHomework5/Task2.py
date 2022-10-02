# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

print('\t\tПРИВЕТ - ЭТА ИГРА КТО ВЫТЯНЕТ ПОСЛЕДНЮЮ КОНФЕТУ')

name = input('Введите ваше имя: ')

def check():
    while True:
        x = int(input('\tЕсли хочешь сыграть с ботом нажми 1, с другим человеком нажми 2: ')) 
        if x == 1 or x == 2:   
            return x
        else:
            print('Неверный ввод')
choose = check()

#choose = int(input('\tЕсли хочешь сыграть с ботом нажми 1, с другим человеком нажми 2: '))

'''Игра с ботом'''
if choose == 1:
    print('Вы выбрали режим игры с ботом')
    sweet = int(input('Введите сколько будет конфет на столе: '))
    one_step = int(input('Введите сколько конфет можно взять за раз: '))
    first_step = True if random.randint(1,2) == 1 else False

    while sweet > 0:
        if first_step == True:
            if sweet >= 5:
                bot_step = random.randint(1, one_step)
                sweet -= bot_step
                print(f"Бот взял {bot_step} конфет, осталось {sweet}")
            elif sweet < 5:
                bot_step = 1
                sweet -= bot_step
                print(f"Бот взял {bot_step} конфет, осталось {sweet}")
                if sweet == 0:
                    print('Бот проиграл!')
                    break
            player_step = int(input(f'Введите сколько конфет вы возьмете от 1 до {one_step}: '))
            sweet -=player_step
            print(f"Игрок взял {player_step} конфет, осталось {sweet}")
            if sweet == 0:
                print(f'{name} проиграл(a)!')
                break
        else:
            player_step = int(input(f'Введите сколько конфет вы возьмете от 1 до {one_step}: '))
            sweet -= player_step
            print(f"Игрок взял {player_step} конфет, осталось {sweet}")
            if sweet == 1:
                print(f'{name} проиграл(a)!')
                break
            if sweet >= 5:
                bot_step = random.randint(1, one_step)
                sweet -= bot_step
                print(f"Бот взял {bot_step} конфет, осталось {sweet}")
            elif sweet < 5:
                bot_step = 1
                sweet -= bot_step
                print(f"Бот взял {bot_step} конфет, осталось {sweet}")
                if sweet == 0:
                    print('Бот проиграл!')
                    break

'''Игра с другим игроком'''
if choose == 2:
    print('Вы выбрали режим игры с другим игроком')
    name2 = input('Введите имя второго игрока: ')
    sweet = int(input('Введите сколько будет конфет на столе: '))
    one_step = int(input('Введите сколько конфет можно взять за раз: '))
    first_step = True if random.randint(1,2) == 1 else False

    while sweet > 0:
        if first_step == True:
            player1_step = int(input(f'{name} сколько конфет вы возьмете от 1 до {one_step}: '))
            sweet -=player1_step
            print(f"{name} взял {player1_step} конфет, осталось {sweet}")
            if sweet == 0:
                print(f'{name} проиграл(a)!')
                break
            player2_step = int(input(f'{name2} сколько конфет вы возьмете от 1 до {one_step}: '))
            sweet -=player2_step
            print(f"{name2} взял {player2_step} конфет, осталось {sweet}")
            if sweet == 0:
                print(f'{name2} проиграл(a)!')
                break

        else:
            player2_step = int(input(f'{name2} сколько конфет вы возьмете от 1 до {one_step}: '))
            sweet -=player2_step
            print(f"{name2} взял {player2_step} конфет, осталось {sweet}")
            if sweet == 0:
                print(f'{name2} проиграл(a)!')
                break
            player1_step = int(input(f'{name} сколько конфет вы возьмете от 1 до {one_step}: '))
            sweet -=player1_step
            print(f"{name} взял {player1_step} конфет, осталось {sweet}")
            if sweet == 0:
                print(f'{name} проиграл(a)!')
                break

print('Спасибо за игру!')
        