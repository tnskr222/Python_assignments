# endless iterator using generator method to produce terms of Fibonacci series

def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

it = fibonacci()
fibonnaci_list = []
while True:
    b = input("Do you want to generate another element [y/n]")
    if b=='y':
        fibonnaci_list.append(next(it))
        print(fibonnaci_list)
    else:
        break