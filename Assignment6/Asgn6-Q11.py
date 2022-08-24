# python script to take the month value in numeric format and display the number of days in it.

a = int(input("enter month number "))
b = int(input("enter year number "))

if a==2 and b%4==0:
    print("Given month has 29 days")
elif a==2 and b%4!=0:
    print("Given month has 28 days")
elif a in (1,3,5,7,8,10,12):
    print("Given month has 31 days")
elif a in (4,6,9,11):
    print("Given month has 30 days")
else:
    print("Given month is not valid")