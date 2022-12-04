# python script to handle a ValueError

import math


def num_stats(x):

    try:
        if x < 0:
            raise ValueError()

        print(f'{x} square root is {math.sqrt(x)}')
    except ValueError:
        print("Please Enter a positive number")
        
num_stats(int(input('Enter a number : ')))