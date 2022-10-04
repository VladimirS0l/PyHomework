# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


list_a = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find_str = 'qwe'
try:
    a = list(filter(lambda tuple: tuple[0] == find_str, zip(
        list_a, range(len(list_a)))))
    print(f'Позиция второго вхождения "qwe": {a[1][1]}')
except:
    print('Второе вхождение "qwe" не найдено')

list_b = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
find_strb = "йцу"
try:
    b = list(filter(lambda tuple: tuple[0] == find_strb, zip(
        list_b, range(len(list_b)))))
    print(f'Позиция второго вхождения "йцу": {b[1][1]}')
except:
    print('Второе вхождение "йцу" не найдено')

list_с = ["йцу", "фыв", "ячс", "цук", "йцукен"]
find_strс = "йцу"
try:
    с = list(filter(lambda tuple: tuple[0] == find_strс, zip(
        list_с, range(len(list_с)))))
    print(f'\nПозиция второго вхождения "йцу": {c[1][1]}')
except:
    print('Второе вхождение "йцу" не найдено')

list_d = ["123", "234", 123, "567"]
find_strd = "123"
try:
    d = list(filter(lambda tuple: tuple[0] == find_strd, zip(
        list_d, range(len(list_d)))))
    print(f'\nПозиция второго вхождения "123": {d[1][1]}')
except:
    print('Второе вхождение "123" не найдено')

list_e = ["123", "234", 123, "567"]
find_stre = "123"
try:
    e = list(filter(lambda tuple: tuple[0] == find_stre, zip(
        list_e, range(len(list_e)))))
    print(f'\nПозиция второго вхождения "123": {e[1][1]}')
except:
    print('Второе вхождение "123" не найдено')
