# Create a generator to produce squares of first N natural numbers

a = int(input('Enter number squares of  natural numbers to produce : '))

def squares(a):
    x=1
    while a:
        yield x**2
        x=x+1
        a-=1
for e in squares(a):
    print(e, end=' ')