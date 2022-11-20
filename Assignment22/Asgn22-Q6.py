# recursive python function to calculate the factorial of a number.

a = int(input('Enter a number to calculate factorial : '))

def factorial(a):
    if a <=1:
        return 1
    b = a*factorial(a-1)
    return b

print(factorial(a))