# python program to create a function that prints the even numbers from a given list.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def evennumbers(c):
    print("Even numbers in the given lisr is : ", end =' ')
    for i in c:
        if i%2==0:
            print(i, end=' ')

evennumbers(list1)