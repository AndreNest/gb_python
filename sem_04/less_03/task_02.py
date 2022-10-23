from argparse import RawDescriptionHelpFormatter


# list = []
# for i in range(1, 21):
#     if(i % 2 == 0):
#         list.append(i)

# print(list)
# list1 = [i for i in range(1,21)]
# print(list1)
# list2 = [i for i in range(1,21) if i%2 == 0]
# print(list2)
# #кортежи
# list3 = [(i,i) for i in range(1,21) if i%2 == 0]
# print(list3)
# # с функцией
# def f(x):
#     return x**3

# list4 = [f(i) for i in range(1,21) if i%2 == 0]
# print(list4)
# list5 = [(i,f(i)) for i in range(1,21) if i%2 == 0]
# print(list5)

list = [i for i in range(1,21)]
print(list)

def f(x):
    return x**3

list1 = [(i,f(i)) for i in range(1,11)]
print(list1)

