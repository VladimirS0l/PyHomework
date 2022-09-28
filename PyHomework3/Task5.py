# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(num): 

    pos_fib_list = []
    fib1 = 0
    fib2 = 1
    for i in range(num + 1):
        if i == 0: pos_fib_list.insert(i, fib1)
        elif i == 1: pos_fib_list.insert(i, fib2)
        else:
            pos_fib_list.insert(i, fib1 + fib2)
            temp = fib2
            fib2 = fib1 + fib2
            fib1 = temp
    return pos_fib_list
pos_fib = fibonacci(int(input('Enter N: ')))
print(pos_fib)

def negafibonacci(num):
    neg_fib_list = []
    fib1 = 1
    fib2 = -1
    for i in range(num + 1):
        if i == 0: neg_fib_list.insert(i, fib1)
        elif i == -1: neg_fib_list.insert(i, fib2)
        else:
            neg_fib_list.insert(i, fib1 - fib2)
            temp = fib2
            fib2 = fib1 - fib2
            fib1 = temp
    return neg_fib_list
neg_fib = negafibonacci(int(input('Enter N: ')))
print(neg_fib)

print(str(f'\n{neg_fib[::-1] + pos_fib}'))





