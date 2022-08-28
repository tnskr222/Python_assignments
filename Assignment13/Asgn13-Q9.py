# Python script to create a list of city names taken from the user.

a = int(input("Number of cities : "))
b=[]

for c in range(a):
    d=input("Enter city name")
    b.append(d)
print(b)