# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число = '))
m = ''
while n > 0:
    m = str(n % 2) + m
    n = n // 2
print(m)

# Задачу также можно решить через функцию bin
# n = int(input('Введите число = '))
# # print(bin(n))