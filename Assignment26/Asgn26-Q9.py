# python script to join 2 threads after printing completing the first Question.

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

a.join()
b.join()

print('bye')