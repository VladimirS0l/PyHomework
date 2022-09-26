# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, 
# но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

def check_input(inputed):
    is_correct = False
    while not is_correct:
        try:
            number = int(input(f'{inputed}'))
            is_correct = True
        except ValueError:
            print('Некорректный ввод')
    return number

num = check_input('Введите число: ')
pali = str(num)

pali1 = pali
pali2 = None
count = 0
while True:
    count += 1
    pali2 = ''.join(reversed(pali1))
    if pali1 == pali2:
        print('Палиндром:', pali2)
        print(f'Количество итераций: {count}')
        break
    else:
        p = int(pali1) + int(pali2)
        pali1 = str(p)
