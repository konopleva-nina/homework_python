'''ЗАДАЧА 16. Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
Задача 18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X'''

import random
size = int(input('Введите размер списка: '))
my_list = []
for _ in range(size):
    my_list.append(random.randint(0, 10))
print(my_list)

number = int(input('Введите число a для определени вхождения в список: '))
count = 0
min = abs(my_list[0] - number)
index = 0
for i in range(len(my_list)):
    if (my_list[i] == number):
        count += 1
    else:
        raznost = abs(my_list[i] - number)
        if (raznost < min):
            min = raznost
            index = i

print(f'\nКоличество вхождений числа a: {count}')
print(f'Самый близкий по величине элемент к числу a (выводим первое вхождение такого элемента): {my_list[index]}')