# python script to calculate sum of first N odd natural numbers

a = int(input("enter a number : "))
b = 0

for a in range(1,(2*a+1),2):
    b+=a
print(f"Sum of first {a} odd natural numbers is {b}")