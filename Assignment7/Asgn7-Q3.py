""" Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.  """

a = int(input("Enter length of first side of triangle : "))
b = int(input("Enter length of second side of triangle : "))
c = int(input("Enter length of third side of triangle : "))

if a==b==c:
    print("Given numbers are the sides of equilateral triangle")
elif a==b!=c or b==c!=a or a==c!=b:
    print("Given numbers are the sides of isoceles triangle")
elif (a*a)==((b*b)+(c*c)) or (b*b)==((a*a)+(c*c)) or (c*c)==((b*b)+(a*a)):
    print("Given numbers are the sides of right angled triangle")
else:
    print()