# recursive python function to print first N natural numbers in reverse order

a = int(input("Enter number of natural numbers : "))

def narural(a):
    if a>0:
        print(a, ' ', end='')
        narural(a-1)        
b = narural(a) 