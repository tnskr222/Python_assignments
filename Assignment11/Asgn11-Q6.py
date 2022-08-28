# python script to calculate factorial of a given number

a = int(input("enter a number : "))
b = 1
for a in range(1,a+1,1):
    b*=a
    print(b,end =' ')
print(f"Factorial of given number {a} is {b}")