# Python script to store a list of city names in a file ‘cities.txt’


def cities():
    f = open("cities.txt", "w+")
    a = int(input("Enter number of cities you want to add to list : "))
    b =[]
    while a>0:
        b.append(input("Enter city name : "))
        a =a-1
    f.write(','.join(b))
    f.close()
    f = open("cities.txt", "r")
    print(f.read())
    f.close()

cities()