# python script to check whether a given pair of numbers are co-Prime numbers or not.

a =int(input("Enter first number : "))

b =int(input("Enter second number : "))
count=1
c = min(a,b)
for i in range(1,c+1):
    if a%i==0 and b%i==0:
        count+=1
if count<=2:
    print(f"Given numbers {a}, {b} are co-prime numbers")
else:
    print(f"Given numbers {a}, {b} are  not co-prime numbers")