from threading import Thread
from time import sleep
#def display():   It can be created by using functions and classes
class Alphabets(Thread):
    def run(self):
        for i in range(65,91):
            print(chr(i))
            sleep(1)

#t=Thread(target=display,name='Alphabets')
t=Alphabets()
t.start()
for i in range(65,91):
    print(i)
    sleep(1)
t.join()