# recursive python function to find the Nth term of the Fibonacci series

a = int(input('Enter the number of the term required in Fibonacci series :'))

def Fibonacci(a):
    if a ==1:
        return 0
    elif a ==2:
        return 1
    else:
        return Fibonacci(a-1)+Fibonacci(a-2)

print(Fibonacci(a))