# python program to create a function which expects a list as an argument.

def f(*list):
    print(*list)

a = [1,2,2,4]
f(*a)