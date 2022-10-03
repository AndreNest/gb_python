# 3. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Число N вводится пользователем. Позиции хранятся в файле file.txt в одной строке одно число
# Позиции в файл вам нужно программно положить в файл в зависимости от выбранного N: если пользователь введет двойку,
#  то в файле вряд ли будут индексы 5 или 16. 
# В решении должны быть и запись в файл, и чтение из файла.
import os
import random
os.system("cls")
def get_number(input_sring):
    try:
        num = int(input(input_sring))
        return num
    except(ValueError):
        return get_number()

def list_random(num):
    list_element = []
    for i in range(num):
        list_element.append(random.randint(-num, num))
    return list_element
def write_file(num):
    f = open('text.txt', 'w')
    ind_1, ind_2 = str(random.randint(0, num -1)), str(random.randint(0, num -1))
    f.write(ind_1)
    f.write('\n')
    f.write(ind_2)
    f.close
def read_file(list_random):
    x = open('text.txt', 'r')
    index_1, index_2 = int(x.readline()), int(x.readline())
    x.close()
    return list_random[index_1] * list_random[index_2]

number = get_number('Введите количество элементов списка: ')
list_number = list_random(number)
print(f'Список : {list_number} ')
write_file(number)
number_result = read_file(list_number)
print(f'Произведение элементов = {number_result}')



