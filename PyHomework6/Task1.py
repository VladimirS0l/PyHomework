# 1- Определить, присутствует ли в заданном списке строк, некоторое число

from curses.ascii import isdigit


list_a = ['rsrrrsr', 'sdbbdwhbdw1', 'sdsd', '1233a', 'dhshdhs2']
count = 0
for i in list_a:
    c = list(filter(isdigit, i))
    if c != []:
        count += 1
print(f'Числа найдены в {count} строках')
