# recursive python function to print cubes of first N natural numbers

a = int(input("Enter number of cubes of first natural numbers : "))

def narural(a):
    if a>0:
        narural(a-1)
        print((a**3), end=' ')        
b = narural(a) 