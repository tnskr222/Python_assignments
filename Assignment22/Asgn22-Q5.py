# recursive python function to calculate sum of cubes of first N natural numbers

a = int(input('Enter number of cubes of natural numbers sum required : '))

def sum(a):
    if a ==0:
        return 0
    b = (a**3)+sum(a-1)
    return b

print(sum(a))