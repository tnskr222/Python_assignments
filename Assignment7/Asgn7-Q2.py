# menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division

x = int(input("""Enter required Operation to perform  
            Addition enter  1 
            Subtraction enter 2  
            Multiplication enter 3 
            Division enter 4
            Enter value :  """))

match x:
    case 1:
        a = int(input("Enter first number "))
        b = int(input("Enter secondnumber "))
        print(a+b)
    case 2:
        a = int(input("Enter greater number "))
        b = int(input("Enter smaller number "))
        print(a-b)
    case 3:
        a = int(input("Enter first number "))
        b = int(input("Enter second number "))
        print(a*b)
    case 4:
        a = int(input("Enter first number "))
        b = int(input("Enter second number "))
        print(a/b)

