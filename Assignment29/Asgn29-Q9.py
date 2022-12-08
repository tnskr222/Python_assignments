"""Python script to store book data in a file. Book data is in the form of a
dictionary in which book name is the key and price is its value. Use pickle to store
data into a file (say bookfile)"""

import pickle
a ={}
c = True
while c:
    key = input('Enter book name : ')
    price = int(input('Enter book price : '))
    a[key]= price
    b = int(input("Enter 1 if you want to enter data else Enter 0"))
    if b ==1:
        c =True
    else:
        c= False
f = open('file1','wb')
pickle.dump(a,f)
f.close()

h = open('file1','rb')
s = pickle.load(h)
for key in s:
    print(key,':',s[key])
h.close()
