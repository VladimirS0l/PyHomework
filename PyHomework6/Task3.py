# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import math

while True:
    try:
        ab = list(
            map(float, input('Введите координаты точки А(х,у), B(х,у): ').split()))
        break
    except:
        continue


def ab_func(x2, x1): return (x2 - x1) ** 2


ab_distance = round(
    math.sqrt((ab_func(ab[2], ab[0]) + ab_func(ab[3], ab[1]))), 2)
print(f'Расстояние между точками А(х,у) и B(х,у) = {ab_distance}')
