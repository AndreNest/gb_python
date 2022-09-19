def get_int_number(input_string) -> int:
    '''
    Ввод натурального числа, через консоль.
    '''
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        print('Ошибка ввода!')
        return get_int_number(input_string)

def get_float_number(input_string) -> float:
    '''
    Ввод вещественного числа, через консоль.
    '''
    try:
        num = float(input(input_string))
        return num
    except(ValueError):
        print('Ошибка ввода!')
        return get_float_number(input_string)

def factoral(num)->int:
    '''
     Факториал числа 
    '''
    fact = 1
    for i in range(2, num + 1):
        fact *= i
    return fact


