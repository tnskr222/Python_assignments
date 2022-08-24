# python script to print squares of first N natural numbers

N = int(input("Enter number of squares of natural numbers to print : "))
a = 1
while a<=N:
    print(f"square of {a} is {a*a}")
    a+=1