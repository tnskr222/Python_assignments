# python script to calculate sum of first N even natural numbers


a = int(input("enter a number : "))
b = 0

for a in range(2,(2*a+1),2):
    b+=a
print(f"Sum of first {a} even natural numbers is {b}")