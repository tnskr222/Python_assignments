"""Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter or triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides."""

a = int(input('Enter length of first side of triangle : '))
b = int(input('Enter length of second side of triangle : '))
c = int(input('Enter length of third side of triangle : '))

def is_valid_triangle(perimeter):
    def triangle(a,b,c):
        if a+b>c and a+c>b and b+c>a:
            print("triangle is valid")
            perimeter(a,b,c)
        else:
            print("triangle is invalid")
    return triangle

@is_valid_triangle
def perimeter(a,b,c):
    print('Perimeter of Triangle with given sides is : ', a+b+c)

perimeter(a,b,c)
