# Create a generator to produce first n prime numbers

a = int(input("Enter number of prime numbers to produce : "))

def prime(a):
    b =2
    while a:
        for x in range(2,b):
            if b%x==0:
                b=b+1
                break
        else:
            a=a-1
            yield b
            b=b+1


for e in prime(a):
    print(e, end=' ')