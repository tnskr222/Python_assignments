# Python script to remove all non int values from a list.

a=[1,44.5,2+66j,98,"2",45, "hello"]
b =1
d=[]
c=0
while c<len(a):
    if type(a[c])==type(b):
        d.append(a[c])
    c+=1
print(d)