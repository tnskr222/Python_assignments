# Python script to print indices of all occurrences of a given element in a given list.

a =[1,2,8,9,3.5,1,1,1,2,2]
print(a)
c=input("Enter element to print indices : ")
print(f"Indices of given element {c} is : ", end =' ')
for i in range(len(a)) :
    b=a[i]
    if eval(c)==b:
        print(i, end=' ')

