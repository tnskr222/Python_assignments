# python script to calculate sum of digits of a given number

a = int(input("Enter a number : "))
c=0

for b in str(a):
    c+=int(b)
print(f"sum of digits of given number {a} is {c}")