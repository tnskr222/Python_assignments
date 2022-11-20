# recursive python function to print first N odd natural numbers in reverse order

a = int(input("Enter number of odd natural numbers : "))

def narural(a):
    if a>0:
        print((2*a)-1, end=' ')        
        narural(a-1)
b = narural(a) 