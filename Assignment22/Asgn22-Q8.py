# recursive python function to print binary of a given decimal number.

a = int(input('Enter decimal number to print binary number : '))

def binary(a):
    if a >1:
        binary(a//2)
    print(a%2,end='')


binary(a)