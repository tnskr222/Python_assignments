# python program to create a function that checks whether a passed string is palindrome or not.

def palindrome(a):
    if a==a[::-1]:
        print("Given string is Palindrome")
    else:
        print("Given string is not palindrome")

palindrome(input("Enter a string : "))