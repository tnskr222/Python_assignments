# python script to print first N prime numbers

n =int(input("Enter Number pf prime numbers required : "))

a =2
b=10
d = []
while len(d)<n:
    for i in range(a,b):
        for e in range(2,i):
            c=i%e
            if c==0:
                break
        else:
             d.append(i)
        if len(d)==n:
            break
    a=b
    b+=50
for h in d:
    print(h,end=' ')