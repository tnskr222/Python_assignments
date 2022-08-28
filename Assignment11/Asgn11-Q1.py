# python script to calculate sum of first N natural numbers

a = int(input("Enter a number : "))
b = 0

for a in range(1,a+1,1):
    b = b+a
print(f"Sum of first {a} natural numbers is {b}")