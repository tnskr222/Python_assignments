# python script to check whether a given year is a leap year or not.

x =int(input("Enter a year"))

if x%4==0:
    print(f"{x} is a leap year")
else:
    print(f"{x} is not a leap year")