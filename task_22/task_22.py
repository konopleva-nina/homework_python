'''Задача 22. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго
множества. Затем пользователь вводит сами элементы множеств.'''


import random
size_first = int(input('Введите размер первого списка: '))
my_first_list = []
for _ in range(size_first):
    my_first_list.append(random.randint(0, 20))
print(my_first_list)

size_second = int(input('Введите размер второго списка: '))
my_second_list = []
for _ in range(size_second):
    my_second_list.append(random.randint(0, 20))
print(my_second_list)

set_result = set()
for i in my_first_list:
    for j in my_second_list:
        set_result.add(i)
        set_result.add(j)
print(set_result)