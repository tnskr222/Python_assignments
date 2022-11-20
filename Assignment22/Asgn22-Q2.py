# recursive python function to calculate sum of first N odd natural numbers

b = int(input('Enter number of odd natural numbers sum required : '))
a = (2*b)-1

def sum(a):
    if a <=0:
        return 0
    b = a+sum(a-2)
    return b

print(sum(a))