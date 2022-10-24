# python program to create a function to check whether a string is a pangram or not.

import string

def is_pangram(str):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for x in letters:
        if x not in str.lower():
            print("Given string is not pangram")
            break
    else:
        print("Given string is pangram")
    
c =input("Enter a string : ")
is_pangram(c)