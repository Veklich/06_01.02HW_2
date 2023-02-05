# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input('Vvedite kol-vo monet: '))
count0 = 0
count1 = 0
for i in range(n):
    orel_reshka = int(input('Vvedite "0" (esli orel) ili "1" (esli reshka): '))
    if orel_reshka == 0:
        count0 += 1
    elif orel_reshka == 1:
        count1 += 1
    else:
        ('Net takoy bukvy v zagadannom slove')
if count0 < count1:
    print (f'Nuzhno perevernut {count0} monet')
else:
    print (f'Nuzhno perevernut {count1} monety')