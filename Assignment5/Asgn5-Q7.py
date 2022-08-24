# Write a python script which takes a three digit number from the user and displays only its last digit.

a = int(input("Enter three digit number "))

if 99<a<1000  and len(str(a))==3:
    b =int(str(a)[2])
    print(f"Last digit of {a} is {b}")
else:
    print("Given number is not a three digit number")