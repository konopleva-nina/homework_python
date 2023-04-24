'''Задача 26. Напишите программу, которая на вход принимает два числа A и B, и возводит 
число А в целую степень B с помощью рекурсии.'''

def recursia(a, b):
    if b == 0:
        return 1
    result = 1
    for i in range(b):
        result = result * a
    return result

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
print(recursia(a, b))