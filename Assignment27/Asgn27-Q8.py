# python script to implement try except and else block for division

try:
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))

    c =a//b
except ZeroDivisionError:
    print("Cannot divide number with zero")
except ArithmeticError:
    print('Arithmetic error')
except ValueError:
    print("Enter a number")
except Exception:
    print("Unknown error")
else:
    print(c)
finally:
    print('completed')