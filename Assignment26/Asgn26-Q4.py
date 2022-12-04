"""python script to create two Threads. First thread will print all Even numbers
and Second thread will print all Odd numbers till 100"""

from  threading import *
from time import *

class even(Thread): 
    def run(self):
        for i in range (1,101):
            if i%2==0:
                print(i, end =' ')
                sleep(0.5)

class odd(Thread):
    def run(self):
        for i in range (1,101):
            if i%2!=0:
                print(i, end= ' ')
                sleep(0.5)

b = odd()
a = even()


b.start()
sleep(0.2)
a.start()

