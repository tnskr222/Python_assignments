# python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots

# Quadratic equation (ax**2)+bx+c

a = int(input("Enter value of a "))
b = int(input("Enter value of b "))
c = int(input("Enter value of c "))

d = b*b - 4*a*c

if d==0:
    print(f"Given Quadratic equation {a}x^2+{b}x+{c} has two real and equal roots")
elif d>0:
    print(f"Given Quadratic equation {a}x^2+{b}x+{c} has two real and distinct roots")
else:
    print(f"Given Quadratic equation {a}x^2+{b}x+{c} has imaginary roots")