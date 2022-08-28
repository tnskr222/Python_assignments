# python script to check whether a given number is Prime or not

a =int(input("Enter a number : "))
count =1
for i in range(1,a):
    c = a%i
    if c==0:
       count+=1
if a == 1:
    print(f"{a} is not a prime number")
elif count >2:
    print(f"{a} is not a prime number")
elif a == 0:
    print(f"{a} is not a prime number")
else:
    print(f"{a} is a prime number")