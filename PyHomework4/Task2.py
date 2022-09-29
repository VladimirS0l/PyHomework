# 2 - Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
#  Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from random import randint


n = int(input("Введите число: "))
list_n = []
i = 1
while i < n:
    list_n.append(randint(1, 5))
    i += 1
print(list_n)

list_n_without_replay = (list(set(list_n)))
print(list_n_without_replay)

'''второй способ'''
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")