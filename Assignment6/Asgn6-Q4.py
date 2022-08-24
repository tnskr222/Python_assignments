# python script to print greater between two numbers. Print number only once even if the numbers are the same.

x = int(input("Enter first number "))
y = int(input("Enter second number "))

if x>y:
    print(f"{x} is greater number ")
elif x==y:
    print(f"{x} is greater number ")
else:
    print(f"{y} is greater number")