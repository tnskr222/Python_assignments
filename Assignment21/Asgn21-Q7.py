# recursive python function to print squares of first N natural numbers

a = int(input("Enter number of squares of first natural numbers : "))

def narural(a):
    if a>0:
        narural(a-1)
        print((a**2), end=' ')        
b = narural(a) 