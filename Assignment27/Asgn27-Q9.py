# python script to raise a ValueError.

try:
    a = int(input('Enter a number : '))
    if a==1:
        raise ValueError()
except ValueError:
    print('Enter a positive or negative numbers')
