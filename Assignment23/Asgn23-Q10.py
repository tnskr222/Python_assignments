"""Define a function which calculates HCF of two numbers. Define and apply a
decorator to check whether two given numbers are co-prime or not."""


a = int(input('Enter first number : '))
b = int(input('Enter second number : '))

def HCF(numbers):
    def co_primes(a,b):
        for i in range(a+1,1,-1):
            if a%i==0 and b%i==0:  
                print ('Given numbers are not co-primes')
                numbers(a,b)
                break
        else:
            print('Given numbers are co-primes')
    return co_primes

@HCF
def numbers(a,b):
    for i in range(a+1,1,-1):
        if a%i ==0 and b%i==0:
            print ('HCF of given numbers is : ', i)
            break
numbers(a,b)