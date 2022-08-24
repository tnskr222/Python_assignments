"""python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year"""

a = int(input("Enter year : "))

if a%400!=0 and a%100!=0 and a%4==0:
    print(f"{a} is Non century leap year")
elif a%400==0:
    print(f"{a} is Century leap year")
elif a%4!=0 and a%100!=0:
    print(f"{a} is Non century non leap year")
else:
    print(f"{a} is Century non leap year")