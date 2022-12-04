# python script to multiple 2 or 3 or 4 numbers with a single multiply method in a class using method overloading.

class multiply:

    def multiplication(self,a,b,c=1,d=1):
        return a*b*c*d

a = multiply()
print(a.multiplication(5,6))
print(a.multiplication(5,6,8))
print(a.multiplication(5,6,10,10))
