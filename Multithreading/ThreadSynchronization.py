from threading import *
from time import *
def display(str1):
    l.acquire()
    for x in str1:
        print(x)
        sleep(1)
    l.release()

l=Lock()
t1=Thread(target=display,args=("HELLO WORLD"))
t2=Thread(target=display,args=("you are welcome"))
t1.start()
t2.start()
t1.join()
t2.join()


from threading import *
from time import *
def display(str1):
    l.acquire()
    for x in str1:
        print(x)
        sleep(1)
    l.release()

l=Semaphore(1)       #This is used to use multiple threads at a time
t1=Thread(target=display,args=("HELLO WORLD"))
t2=Thread(target=display,args=("you are welcome"))
t1.start()
t2.start()
t1.join()
t2.join()