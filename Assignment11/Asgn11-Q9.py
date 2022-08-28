# python script to print binary equivalent of a given decimal number. (do not use bin() method)

a = int(input("Enter number : "))
d = []
count = 1
while a>=0:
    b=a%2
    a=a//2
    d.append(b)
    if a==0:
        count+=1
        if count==2:
            break
d.reverse()
for i in d:
    print(i,end=' ')