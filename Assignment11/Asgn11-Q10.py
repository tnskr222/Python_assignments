# python script to print the octal equivalent of a given decimal number. (do not use oct() method)

a = int(input("Enter number : "))
d = []
count = 1
while a>=0:
    b=a%8
    a=a//8
    d.append(b)
    if a==0:
        count+=1
        if count==2:
            break
d.reverse()
for i in d:
    print(i,end=' ')