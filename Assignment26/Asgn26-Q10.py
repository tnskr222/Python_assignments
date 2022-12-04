"""python script to check whether a given number is prime or armstrong number
using 2 different threads"""

from  threading import *
from time import *




class prime(Thread):

    a = int(input("Enter a number : "))
    def run(cls):
        for i in range(2,cls.a):
            if cls.a%i==0 and cls.a>1:
                break
        else:
            print('Given number is Prime number')
        sleep(5)

class armstrong(prime,Thread):

    def run(cls):
        super().run()
        b=len(str(cls.a))
        # initialize sum
        sum = 0

        # find the sum of the cube of each digit
        temp = cls.a
        while temp > 0:
            digit = temp % 10
            sum += digit ** b
            temp //= 10

        # display the result
        if cls.a == sum:
            print(cls.a,"is an Armstrong number")
        else:
            print(cls.a,"is not an Armstrong number")


thread1 = prime()
thread2 = armstrong()

thread1.start()
thread2.start()