# python script to print first N odd natural numbers

a=1
b=1
N = int(input("Enter number of first odd naturals numbers to print : "))
while b<=N:
    print(a, end = " ")
    a+=2
    b+=1