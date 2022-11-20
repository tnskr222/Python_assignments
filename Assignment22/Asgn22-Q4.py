# recursive python function to calculate sum of squares of first N natural numbers

a = int(input('Enter number squares of natural numbers sum required : '))

def sum(a):
    if a ==0:
        return 0
    b = (a*a)+sum(a-1)
    return b

print(sum(a))