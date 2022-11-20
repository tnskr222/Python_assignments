# recursive python function to print first N natural numbers

a = int(input("Enter number of natural numbers : "))

def narural(a):
    if a>0:
        narural(a-1)
        print(a, end=' ')        
b = narural(a) 