# python script which takes a three digit number from the user and displays only its first digit.

a = int(input("Enter three digit number "))

if 99<a<1000 and len(str(a))==3:
    b =int(str(a)[0])
    print(f"First digit of {a} is {b}")
else:
    print(f"Given number {a} is not a three digit number")