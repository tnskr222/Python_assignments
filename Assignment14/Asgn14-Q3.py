# Python script to create a list of first N even natural numbers.

a =int(input("Enter number of natural numbers : "))
b=[]
for i in range (2,2*a+1,2):
    b.append(i)
print(b)