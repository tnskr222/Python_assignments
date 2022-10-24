# python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def checkprime(a):

    if a>1:
        for i in range(2,a):
            if a%i==0:
                print("Number is not prime")
                break
        else:
            print("Number is prime")
    else:
        print("Number is not prime")

checkprime(int(input("Enter a number")))