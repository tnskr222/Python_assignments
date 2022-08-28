# Python script to create a list, where each element of the list is a digit of a given number.

a =int(input("Enter a number : "))
c=[]
for d in str(a):
    c.append(eval(d))
print(c)
