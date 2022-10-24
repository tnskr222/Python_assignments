# python program to create a function which expects an unknown number of arguments.

def f(*args):
    print(*args)
f('a',1,'b')