# python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)

tuple1=(1,2,3,4,5,6)
a = tuple([b for b in tuple1[3:5:1]])
print(f"a = {a}")
