# Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел. 
# НОК - наименьшее общее кратное, которое делится и на первое, и на второе число
import random
import os
os.system('clear')

num_1 = int(input('Введите первое число: '))
num_2 = int(input('введите второе число: '))
if num_1 > num_2:
    num_1, num_2 = num_2, num_1
for i in range(1, num_2+1):
    if (num_1 * i) % num_2 == 0:
        print(f' НОК = {num_1 * i}')
        break
