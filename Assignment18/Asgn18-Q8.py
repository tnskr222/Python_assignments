# python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.

key_items = ['name', 'age', 'experience', 'qualification']
value_items = ['suresh', 22, '1 year', 'Mtech']
d = {}
for i in range(len(key_items)):
    d[key_items[i]]=value_items[i]
print(d)