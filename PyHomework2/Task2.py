# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#*Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)



# n = int(input("Введите N: "))
# multiplicationN = 1
# for i in range(1, n + 1):
#     multiplicationN *= i
#     print(multiplicationN, end= ', ')


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

list_factorial = []
for i in range(1, num + 1):
    if i == 1:
        list_factorial = [i]
        continue
    else:
        list_factorial.append(list_factorial[i-2] * i)

print(list_factorial)