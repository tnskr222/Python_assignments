# python script to create 2 threads to add all the values from 1 to 100.

from  threading import *
from time import *

class add(Thread):

    def run(self):
        c =0
        for i in range (1,101):
                c= c+i
                sleep(0.1)
        print(c)


class add2(Thread):
    
    def run(self):
        c = 0
        for i in range (1,101):
                c= c+i
                sleep(0.1)
        print(c)

a = add()
d =add2()

a.start()
sleep(0.5)
d.start()


