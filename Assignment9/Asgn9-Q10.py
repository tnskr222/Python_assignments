# python script to print first 10 multiples of N

a = 1
N = int(input("Enter number  : "))
while a<=10:
    print(f"{N} * {a} = {N*a}")
    a+=1