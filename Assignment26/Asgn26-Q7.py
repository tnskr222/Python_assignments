"""python script to create a clock where 1st thread will print the current time
every second and 2nd will print “1 Minute Completed” after every 1 minute"""

from  threading import *
from time import *
from datetime import datetime
import time



class second(Thread):
    def run(self):
        while 1:
            print(strftime("%H:%M:%S", gmtime()))
            time.sleep(1)

class minute(Thread):
    def run(self):
        while 1:
            print('one minute completed')
            time.sleep(60)


b= second()
c= minute()

b.start()
sleep(60)
c.start()

