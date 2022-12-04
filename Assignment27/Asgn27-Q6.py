# python script to create a calculator with 4 basic operations, and handle a maximum number of exceptions.

try:
    a = int(input('Enter a number : '))
    b = int(input("enter a number : "))
    c = a*b
    d = a//b
    e = a-b
    f = a+b

except ZeroDivisionError:
    print('Enter a positive or negative number')
except ArithmeticError:
    print('Arithmetic')
except ValueError:
    print('Enter a number')
except Exception:
    print('Unknown error')
else:
    print(f"Multiplication of {a}, {b} is {a*b}")
    print(f"Division of {a} by {b} is {a//b}")
    print(f"Addition of {a}, {b} is {a+b}")
    print(f"Subtracting {b} from {a} gives {a-b}")