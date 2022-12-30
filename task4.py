# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
os.system('cls')
from random import randint

k = int(input('Введите натуральную степень k: '))
list_b = []
list_k = []
res_list = []
for i in range(k,-1,-1):
    list_b.append(randint(0, 50))
    list_k.append(i)
for i in range(k+1):    
    if i==k:
        res_list.append(str(list_b[i]))
    elif i==k-1:
        res_list.append(str(list_b[i])+'x')
    else:
        res_list.append(str(list_b[i])+'x^'+str(list_k[i]))
    if i == k:
        print(res_list[i], end='=0')
    else:
        print(res_list[i], end='+')
text='=0'
data = open('file.txt', 'a') 
data.write("+".join(res_list)+"".join(text))  
data.close()     