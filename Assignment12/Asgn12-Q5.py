# python script to find next prime number of a given number
a =int(input("enter a number : "))
while a<1:
    a+=1
a+=1
for i in range(2,a):
    if a%i==0:
        break
else:
    print(f"{a} is  the next prime number")