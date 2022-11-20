# recursive python function to print first N multiples of a given number.

c = int(input("Enter a number : "))
a = int(input("Enter number of multiples of given number : "))

def narural(a):
    if a>0:
        narural(a-1)
        print(c,'*',a,'=',c*a)        
b = narural(a) 