# python script to print first N even natural numbers in reverse order


N = int(input("Enter number of first Even natural numbers to print in reverse order : "))
a =(N*2)
b=1
while b<=N:
    print(a, end =" ")
    a-=2
    b+=1