# Python script to create a list of first N natural numbers.

a =int(input("Enter number of natural numbers : "))
b=[]
for i in range (1,a+1):
    b.append(i)
print(b)