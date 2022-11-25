# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
mas = []
for i in range(int(input('Введите длину списка = '))):
    mas.append(random.uniform(1, 5))
print(mas)
max = mas[0]%1
for i in range(len(mas)):
    if mas[i]%1 > max:
        max = mas[i]%1
print(max)
min = mas[0]%1
for i in range(len(mas)):
    if mas[i]%1 < min:
        min = mas[i]%1
print(min)
print(f"разница между максимальным и минимальным значением дробной части элементов = {max-min}")
