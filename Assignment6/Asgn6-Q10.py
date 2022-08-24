# python script to print greater among three numbers. Print number only once even if the numbers are the same.

x = int(input("Enter first number "))
y = int(input("Enter second number "))
z = int(input("Enter third number "))

if x>y and x>z:
    print(f"{x} is greater number ")
elif x==y==z:
    print(f"{x} is greater number ")
elif y>x and y>z:
    print(f"{y} is greater number")
elif z>x and z>y:
    print(f"{z} is greater number")
elif z==x and z>y:
    print(f"{z} is greater number")
elif z==y and z>x:
    print(f"{z} is greater number")
elif x==y and x>z:
    print(f"{x} is greater number")