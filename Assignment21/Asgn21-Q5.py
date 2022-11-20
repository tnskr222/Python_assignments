# recursive python function to print first N even natural numbers.


a = int(input("Enter number of natural natural numbers : "))

def narural(a):
    if a>0:
        narural(a-1)
        print((2*a), end=' ')        
b = narural(a) 