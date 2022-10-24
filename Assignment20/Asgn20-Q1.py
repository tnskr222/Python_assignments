# python program to create a function that takes a list and returns a new list with the original list's unique elements.

list1 = [2,3,5,22,6,77,11,11,11,11,22,22,77,22,77,6]

def unique(c):
    c.reverse()
    d=[]
    for i in c:
        d.append(i)
    for i in c:
        if d.count(i)>1:
            d.remove(i)
    d.reverse()
    print(d)
unique(list1)
