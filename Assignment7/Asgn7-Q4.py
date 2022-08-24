"""Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""

x = int(input("Enter the age of person : "))

if 0<x<10:
    print(f"Person is kid having age of {x}")
elif 10<x<20:
    print(f"Person is Teen having age of {x}")
elif 20<x<40:
    print(f"Person is Young having age of {x}")
elif 40<x<60:
    print(f"Person is Experienced having age of {x}")
else:
    print(f"Person is Experienced having age of {x}")