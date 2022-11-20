# recursive python function to print a number in reverse order

a = int(input("Enter a number : "))
def reverse(a):
    if a>0:
        print(a%10, end ='')
        reverse(a//10)

reverse(a)
