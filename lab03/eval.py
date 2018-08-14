from random import randint, choice

# define
# argument
def calc(x, y, op):
    res = 0
    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        res = x / y
    return res
# call
# result= calc(4, 2, '+')
# print(result)

