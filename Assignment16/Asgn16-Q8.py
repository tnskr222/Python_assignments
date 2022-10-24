# python program to Sort a tuple of tuples by the second item. tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
e = list(tuple1)

len1 = len(e)
for i in range(0,len1):
    for j in range(0, (len1-i-1)):
        if(e[j][1]> e[j+1][1]):
            temp = e[j]
            e[j] = e[j+1]
            e[j+1] = temp
tuple1 = tuple(e)
print(tuple1)
