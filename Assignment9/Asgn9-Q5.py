# python script to print first N odd natural numbers in reverse order
N = int(input("Enter number of first odd natural numbers to print in reverse order : "))
a =(N*2-1)
b=1
while b<=N:
    print(a, end = " ")
    a-=2
    b+=1