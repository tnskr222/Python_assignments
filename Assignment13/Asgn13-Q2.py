# python script to get the data type of a list.
b =1
c =2
d =2.35
e=2+3j
a = [b, c, 'ab12', d, e]
for i in a:
    h=type(i)
    print(f"Data type of {i} is {h}")