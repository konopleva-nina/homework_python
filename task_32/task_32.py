'''Задача 32. Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)'''

import random
size = int(input('Введите размер списка: '))
list = [random.randint(-20, 20) for _ in range(size)]
print(list)
minn = int(input('Введите минимум: '))
maxx = int(input('Введите максимум: '))
list_2 = [i for i in range(size) if minn <= list[i] <= maxx]
print(list_2)