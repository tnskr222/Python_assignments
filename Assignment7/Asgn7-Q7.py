# python program to check whether a given number is positive, negative or zero using match case statement

a = int(input("Enter Number : "))

if a>0:
    b=1
elif a<0:
    b=2
else:
    b=3

match b:
    case 1:
        print("Given number is positive")
    case 2:
        print("Given number is negative")
    case 3:
        print("Given number is zero")

