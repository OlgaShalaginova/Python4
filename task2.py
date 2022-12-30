# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import os
os.system('cls')

n = int(input('Введите число: '))
i = 2
list = []
while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
    else:
        i +=1
print(list)    