# python script to print first N even natural numbers in reverse order
a = int(input("Enter a number : "))

for a in range(2*a,1,-2):
    print(a,end=' ')