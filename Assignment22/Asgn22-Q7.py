# recursive python function to calculate sum of the digits of a given number

a = int(input('Enter number of cubes of natural numbers sum required : '))

def sum(a):
    if a ==0:
        return 0
    b = (a%10)+sum(a//10)
    return b

print(sum(a))