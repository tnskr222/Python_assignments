# Create a generator to produce first n even natural numbers

a = int(input('Enter number of even natural numbers to produce : '))

def even(a):
    x=2
    while a:
        yield x
        x=x+2
        a-=1
for e in even(a):
    print(e, end=' ')