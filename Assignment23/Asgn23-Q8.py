# Create an endless iterator using generator method to produce Prime numbers

def primenumber():
    b =2
    while True:
        for x in range(2,b):
            if b%x==0:
                b=b+1
                break
        else:
            yield b
            b=b+1

it = primenumber()
primenumber_list = []
while True:
    b = input("Do you want to generate another prienumber [y/n]")
    if b=='y':
        primenumber_list.append(next(it))
        print(primenumber_list)
    else:
        break