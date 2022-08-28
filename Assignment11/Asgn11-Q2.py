# python script to calculate sum of squares of first N natural numbers

a = int(input("Enter a number : "))
c = 0

for a in range(1,a+1,1):
    b = a**2
    c+=b
print(f"sum of squares of first {a} natural numbers is {c}")