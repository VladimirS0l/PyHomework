# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите N: "))
list = []
sum = 0
for i in range(1, n + 1):
    m = round((1 + 1 / i)**i, 2)
    sum += m
    list.append(m)

print(list)
print(sum)


# [round((1 + 1 / x)**x, 2) ]

# print(main(n))
# print(round(sum(main(n))))