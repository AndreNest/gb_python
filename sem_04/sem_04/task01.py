# 1. Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

user_str = input('Введите числа через пробел: ')
list_num = user_str.split(' ')
print(f'Максимальное значение: {max(list_num)}, минимальное значение: {min(list_num)}')