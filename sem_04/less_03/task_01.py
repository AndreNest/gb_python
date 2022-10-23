# def sum(x,y):
#     return x+y

# print(sum(5,10))

# sum = lambda x, y: x + y + 5
def calc(op, a, b):
    print(op(a, b))
calc(lambda x, y: x + y, 10, 5)