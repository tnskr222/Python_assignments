# recursive python function to calculate sum of first N even natural numbers

b = int(input('Enter number of even natural numbers sum required : '))
a = (2*b)

def sum(a):
    if a <=0:
        return 0
    b = a+sum(a-2)
    return b

print(sum(a))