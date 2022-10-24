# python program to create a function to check whether a string is an anagram or not.

def is_anagram(a,b):
    list_a=list(a.lower())
    list_b=list(b.lower())
    list_a.sort()
    list_b.sort()
    return(list_a==list_b)

print(is_anagram(input("enter a string : "), input("Enter a string :")))