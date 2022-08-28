# python script to reverse a number.

a = int(input("enter a number: "))
c = []
count=0
while a//10>=0:   
    b=a%10
    a=a//10
    c.append(b)
    if a%10==0:
        count+=1
        if count==1:
            break
for i in c:
    print(i,end='')
