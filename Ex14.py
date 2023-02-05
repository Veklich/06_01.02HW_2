# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('Vvedite chislo: '))
stepen = 0
stepen_dvoyki = 1
while 2**stepen <= n:
    stepen_dvoyki = 2**stepen
    print(stepen_dvoyki, end=' ')
    stepen += 1
