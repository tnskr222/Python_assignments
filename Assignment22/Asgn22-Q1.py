# recursive python function to calculate sum of first N natural numbers

a = int(input('Enter number of natural numbers sum required : '))

def sum(a):
    if a ==0:
        return 0
    b = a+sum(a-1)
    return b

print(sum(a))
