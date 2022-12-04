# python script to change the name of the Thread.

from  threading import *
from time import *
import threading


def thread_1(i):
    sleep(5)
    print('Value by '+ str(threading.current_thread().name)+" is: ", i)

    
# Creating three sample threads 
thread1 = threading.Thread(target=thread_1, args=(10,))
thread1.name = "Thread_number_1"
thread2 = threading.Thread(target=thread_1, args=(20,))

# Running the threads
thread1.start()
sleep(0.2)
thread2.start()
