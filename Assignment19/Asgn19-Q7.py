# python program to sum all the numbers in a list.

list1 = [1,6,5,8,9,50]

def add(numbers):
    b =0
    for x in numbers:
        b+=x
    return b

c = add(list1)
print(c)