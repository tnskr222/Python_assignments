# python script to handle the ArithmeticError

# python script to create a ArithmeticError

a = int(input('Enter a number : '))

try:
    b = int(input("enter a number : "))
    if b ==0:
        raise ArithmeticError()
    c=a//b
    print(c)

except ArithmeticError:
    print('Arithmetic')
finally:
    print('completed')