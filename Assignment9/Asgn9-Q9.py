# python script to print cubes of first N natural numbers

N = int(input("Enter number of squares of natural numbers to print : "))
a = 1
while a<=N:
    print(f"Cube of {a} is {a**3}")
    a+=1