# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random
mas = []
new_mas = []
for i in range(int(input('Введите длину списка = '))):
    mas.append(random.randint(1, 10))
print(mas)
i = 0
for i in range(int(len(mas)/2)+1):
    new_mas.append(int(mas[i]*mas[len(mas)-i-1]))
print(new_mas)