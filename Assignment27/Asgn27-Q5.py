# python script to handle multiple Exception in one try

try:
    a = int(input('Enter a number : '))
    b = int(input("enter a number : "))
    if b ==0:
        raise ArithmeticError()


except ArithmeticError:
    print('Arithmetic')

except ValueError:
    print('Enter a number')
except Exception:
    print('Unknown error')
else:
    c=a//b
    print(c)
finally:
    print('completed')