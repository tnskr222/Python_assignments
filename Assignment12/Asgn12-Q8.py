# python script to print first N terms of a Fibonacci series

a =int(input("enter number of terms required : "))

b=0
c=1

count=0

if a<=0:
    print("Please enter a positive number")
elif a==1:
    print(" Fibonnaci sequencw upto ", a, " : ", b)
else:
    print("Fibonnaci sequence of ", a, "is : ",end =' ' )
    while count<a:
        print(b,end = ' ')
        d =b+c
        b = c
        c=d
        count+=1