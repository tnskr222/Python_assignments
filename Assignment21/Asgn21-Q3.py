# recursive python function to print first N odd natural numbers

a = int(input("Enter number of odd natural numbers : "))

def narural(a):
    if a>0:
        narural(a-1)
        print((2*a)-1, end=' ')        
b = narural(a) 