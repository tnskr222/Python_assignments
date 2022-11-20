# recursive python function to print first N even natural numbers in reverse order.

a = int(input("Enter number of even natural numbers : "))

def narural(a):
    if a>0:
        print((2*a), end=' ')        
        narural(a-1)
b = narural(a) 