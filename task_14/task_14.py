'''Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''

N = int(input('Введите число N: '))
stepen = 1
chislo = 1
while (chislo < N):
    print (chislo, end=" ")
    chislo = 2 ** stepen
    stepen += 1