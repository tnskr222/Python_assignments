# python script to create 5 threads to fill a list with random numbers till 100.

from  threading import *
from time import *
import random


y = []
def task1():
    while len(y)<100:
        y.append(random.randint(0,100))
        sleep(0.5)

b= Thread(target= task1(), name ='b')
c= Thread(target= task1(), name ='c')
f= Thread(target= task1(), name ='f')
d= Thread(target= task1(), name ='d')
e= Thread(target= task1(), name ='e')

b.start()
sleep(0.1)
c.start()
sleep(0.1)
f.start()
sleep(0.1)
d.start()
sleep(0.1)
e.start()


print(y)

