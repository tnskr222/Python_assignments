# Create a generator to produce first n terms of Fibonacci series

c = int(input('Number of terms of Fibonacci series to generate : '))

def fibonacci(c):
    a,b = 0,1
    while c:
        yield a
        a,b = b, a+b
        c=c-1

for e in fibonacci(c):
    print(e, end=' ')