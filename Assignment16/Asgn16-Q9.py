# Write a python program to print the value 20 from given nested tuple tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
n = 0
for a in tuple1:
    for j in a:
        if j==20:
            n+=1
            print(20)
if n==0:
    print("20 is not present in given list")
        