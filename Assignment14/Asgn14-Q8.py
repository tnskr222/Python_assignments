# Python script to print distinct elements along with their frequencies of occurrence in the list.

a =[1,2,'MySirG',3.5,'MySirG',1,1,1,2,2,'MySirG', 6+3j, 6+3j]
c=[]
for i in a:
    b= a.count(i)
    if i not in c:
        c.append(i)
        print(f"Frequency of {i} in the list is {b}")
print(c)