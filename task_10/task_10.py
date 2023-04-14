'''На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
 повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть'''

import random
count = int(input('Введите число монеток: '))
count_0 = 0
count_1 = 0
for i in range(count):
    monetki = random.randint(0, 1)
    print(monetki, end=" ")
    if (monetki == 0):
        count_0 += 1
    if (monetki == 1):
        count_1 += 1
if (count_0 > count_1):
    print(f'\n{count_1}')
else:
    print(f'\n{count_0}')