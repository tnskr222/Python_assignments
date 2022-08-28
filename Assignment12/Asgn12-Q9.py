# python script to calculate LCM of two numbers

a =int(input("Enter first number: "))
b= int(input("Enter second number : "))

for c in range(max(a,b), ((a*b)+1)):
    if c%a==0 and c%b==0:
        break
print(f"LCM of {a}, {b} is : {c}")