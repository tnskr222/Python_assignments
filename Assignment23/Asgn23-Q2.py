# Create a generator to produce first n odd natural numbers

a = int(input('Enter number of odd natural numbers to produce : '))

def odd(a):
    x=1
    while a:
        yield x
        x=x+2
        a-=1
for e in odd(a):
    print(e, end=' ')