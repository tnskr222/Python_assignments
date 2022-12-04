# python script to create a Calculator class with 2 methods for adding and subtracting 2 values.

class Calculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        c = self.a+self.b
        return c

    def sub(self):
        c= self.a-self.b
        return c

a = Calculator(5,7)
print(a.add())
print(a.sub())