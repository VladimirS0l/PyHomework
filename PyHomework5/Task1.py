# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

line = input('Это программа удаляющая из текста все слова содержащие "абв", введите текст: \n')
rline = line.split()
rline = ' '.join(filter(lambda x: 'абв' not in x, rline))
print(f'Оригинальный текст -> {line}\n\nТекст без слов включающие "абв" -> {rline}')

