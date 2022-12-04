"""python script to create a Calculator 2.0 class with 2 methods for multiplication
and division of 2 values and inherit it from the Calculator class."""

class Calculator:

    a = 8
    b = 2

    def multiply(cls):
        c = cls.a*cls.b
        return c

    def division(cls):
        c = cls.a//cls.b
        return c

a = Calculator()

print(a.multiply())
print(a.division())