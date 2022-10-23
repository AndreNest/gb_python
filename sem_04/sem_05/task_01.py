# n - это степень икса первого элемента полинома
# при n =3 => 5*x**3 + 18*x**2 + 7*x + 19 = 0 - коэффициенты = [5,18,7,19]
# n=2 => 2*x² + 4*x + 5 = 0(коэф: [2,4,5]) или x² + 5 = 0 (коэф: [1,0,5]) или 10*x²(коэф: [10,0,0]) = 0
# n=10 => 56 * x**10 = 0
# коэффициенты - это числа перед элементами полинома.
# коэффициенты могут быть нулем, кроме перво
import random


def random_koef(n):
    '''
    Получение .
    '''
    koef_list = []
    for i in range(0, n):
        koef_list.append(random.randint(0,100))
        if i == 0:
            while koef_list[0] == 0:
                del koef_list[0]
                koef_list.append(random.randint(0,100))
    return koef_list

# def gen_polinom(koef_list, n):
#     for i in range(0, len(koef_list)):
#         if koef_list[i] != 0:
#             if koef_list[i] == 1:


def gen_polinom_new(n):
    '''
    Получение списка с Х.
    '''
    list_x = []
    while n > 0:
        if n == 1:
            list_x.append(f'x')
        else:
            list_x.append(f'x^{n}')
        n -= 1
    list_x.append('')
    return list_x
    






def number_input(input_string):
    '''
    Функция для проверки ввода числа.
    '''
    while type:
        digit = input(input_string)
        try:
            digit = int(digit)
            return digit
        except ValueError:
            print("Введено неверное значение. Только числа!!!")

n = number_input('Введите степень полиндрома: ')
random_koef(n)

print(gen_polinom_new(n))