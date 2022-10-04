# Задание с семинара
# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# (256 - 194 => некорректная запись скобок


def list_numbers(expr):
    list_number = []
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
    return list_number


def list_operations(expr):
    list_operation = list(filter(lambda x: x == '/' or x == '*' or x == '+' or x == '-', expr))
    return list_operation


def list_reduce(i, list1, list2):
    del list1[i + 1]
    del list2[i]
    return list1, list2


def expr_operation(list_number, list_operation):
    while len(list_operation) > 0:
        while '/' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '/':
                    list_number[i] = list_number[i] / list_number[i+1]
                    list_reduce(i, list_number, list_operation)
        while '*' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '*':
                    list_number[i] = list_number[i] * list_number[i+1]
                    list_reduce(i, list_number, list_operation)
        while '+' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '+':
                    list_number[i] = list_number[i] + list_number[i+1]
                    list_reduce(i, list_number, list_operation)
        while '-' in list_operation:
            for i, elem in enumerate(list_operation):
                if elem == '-':
                    list_number[i] = list_number[i] - list_number[i+1]
                    list_reduce(i, list_number, list_operation)
    return list_number[0]


expr_to_calc = '3-4*2' #input('Введите выражение для расчета: ')
list_number = list_numbers(expr_to_calc)
list_operation = list_operations(expr_to_calc)
print(f'{expr_to_calc} ->\n{expr_operation(list_number, list_operation)}')

print(eval('3-4*2'))
