# a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.

def calculate(c):
    d=[]
    e=[]
    for i in c:
        if ord('A')<=ord(i)<=ord('Z'):
            d.append(i)
    for i in c:
        if ord('a')<=ord(i)<=ord('z'):
            e.append(i)
    print(f"Number of upper case letters is : {len(d)}, {d}")
    print(f"Number of lower case letters is : {len(e)}, {e}")

calculate(input("Enter a string : "))