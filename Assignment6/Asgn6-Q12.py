# python script to accept one complex number from the user and display the greater number between real part and imaginary part

a = complex(input("Enter complex number "))

if a.real>a.imag:
    print("real part  is the greater number = {a.real}")
elif a.real==a.imag:
    print("real part  and imaginary part are equal i= {a.real}")
else:
    print("imaginary part  is the greater number = {a.imag}")