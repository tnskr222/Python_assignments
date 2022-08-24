# python script to check whether a given number is a three digit number or not.

x = int(input("Enter three digit number "))

if 99<x<1000:
    print(f"{x} is a three digit number")
else:
    print(f"{x} is not a three digit number")