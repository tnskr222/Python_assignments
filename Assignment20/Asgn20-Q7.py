# python program to access a function inside a function.

def factorial(b):
    def multiplication(a):
        nonlocal b
        d=1
        for i in range(1,b+1):
            d*=i
        return d
    return multiplication
f = factorial(8)
print(f(8))