# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

mas = []
for i in range(5):
    mas.append(random.randint(1, 10))
print(mas)
new_mas = []
sum = 0
for i in range(len(mas)):
    if (i % 2) != 0:
        new_mas.append(int(mas[i]))
        sum += mas[i]
print('')
print(f"На нечетных позициях {new_mas}, ответ: {sum}")

