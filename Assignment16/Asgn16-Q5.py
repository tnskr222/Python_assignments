# python program to check if all items in the tuple are the same.

a = (10,'MySirG',10,10)
b = a[1]
for i in a:
    if i != b:
        print("All items in a are not same")
        break
else:
    print("All elements in a are same")