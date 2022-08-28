# python script to print all Prime numbers between two given numbers (both values inclusive)

a =int(input("Enter first number : "))

b =int(input("Enter second number : "))

while a<=1:
    a+=1
    
for i in range(a,b+1):
    for c in range(2,i):
        d = i%c
        if d==0:
                break
    else:
        print(i,end = ' ')
    