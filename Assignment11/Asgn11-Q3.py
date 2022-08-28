# python script to calculate sum of cubes of first N natural numbers

a = int(input("Enter a number : "))
c = 0

for a in range(1,a+1,1):
    b = a**3
    c+=b
print(f"sum of cubes of first {a} natural numbers is {c}")