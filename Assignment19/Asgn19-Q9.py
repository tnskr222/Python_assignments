# python program to create a function to check whether a number falls in a given range.

def check(c):
    a = int(input("Enter a lesser number : "))
    b = int(input("Enter a larger number : "))
    if a <= c <=b:
        print("Number falls in given range")
    else:
        print("Number not falls in given range ")

check(8)
