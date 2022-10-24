# python program to multiply all the numbers in a list.
list1 = [1,6,5,8,9]

def multiply(numbers):
    b =1
    for x in numbers:
        b*=x
    return b

c = multiply(list1)
print(c)