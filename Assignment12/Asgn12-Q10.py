# python script to calculate HCF of two numbers

a = int(input("Enter first number : "))
b = int(input("Enter Second number : "))

for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
        break
print(f"HCF of {a}, {b} is : {i}")