# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 
# до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей,
#  состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова
#  имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его
#   номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
#  Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе 
# с преобразованным списком

languege = ['C#', 'Python', 'Java', 'JavaScript', 'C++', 'Delphi', 'Visual Basic']
numbers = [1, 2, 3, 4, 5, 6, 7]

result = list(zip(numbers, languege))
print(result)




