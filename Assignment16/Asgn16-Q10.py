""" Write a python program to change the first item (22) of a list within the following tuple
to 222.
tuple1 = (11, [22, 33], 44, 55) """

tuple1 = (11, [22, 33], 44, 55)
e = list(tuple1)

for i in tuple1:
    if type(i) is list:
        for a in i:
            if a ==22:
                i.remove(22)
                i.insert(0,222)

print(e)