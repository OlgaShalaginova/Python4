# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

import os
os.system('cls')
from random import randint

num = int(input('Введите число элементов: '))
list_num = []
for i in range(num):
    list_num.append(randint(0, 10))
print('Первоначальный список:', list_num)
list_2 = []
for i in range(len(list_num)):
    count = 1
    for j in range(i+1, len(list_num)):
        if list_num[j] == list_num[i]:
            count += 1
    for j in range(0, i):
        if list_num[j] == list_num[i]:
            count += 1
    if count == 1:
        list_2.append(list_num[i])
print('Неповторяющиеся элементы:', list_2)