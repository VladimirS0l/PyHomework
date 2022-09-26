# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime 
# (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import math, datetime

def random(_min,_max):
    d = _max - _min
    ms = datetime.datetime.today().microsecond/(10**6)
    print(f'{ms=}')
    return _min + math.ceil(d * ms)

print(random(1, 20))
