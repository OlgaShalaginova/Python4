# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import os
os.system('cls')

d = int(input('Введите разрядность: '))
pi = 3
sum =0
for i in range(2,10000000,4):
    pi1 =4/(i*(i+1)*(i+2)) - 4/((i+2)*(i+3)*(i+4))    
    sum += pi1 
res = str(pi+sum)
res1=res[:2+d]
print(res1)