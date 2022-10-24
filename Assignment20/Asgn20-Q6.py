# python program to create a function and print a list where the values are square of numbers between 1 and 30.

def squares():
    a = [x**2 for x in range(31)]
    print(a)

squares()