# python script to print first N odd natural numbers in reverse order

a = int(input("Enter a number : "))

for a in range(2*a-1,0,-2):
    print(a,end=' ')