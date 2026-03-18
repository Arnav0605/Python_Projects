from threading import Thread, Condition
from time import sleep

class MyData:
    def __init__(self):
        self.data = None
        self.flag = False
        self.cond = Condition()

    def put(self, d):
        with self.cond:
            while self.flag:
                self.cond.wait()
            self.data = d
            self.flag = True
            self.cond.notify()

    def get(self):
        with self.cond:
            while not self.flag:
                self.cond.wait()
            x = self.data
            self.flag = False
            self.cond.notify()
            return x


def producer(data, count=10):
    for i in range(1, count + 1):
        data.put(i)
        print('Producer:', i)
        sleep(0.05)
    # send sentinel to signal consumer to exit
    data.put(None)


def consumer(data):
    while True:
        x = data.get()
        if x is None:
            break
        print('Consumer:', x)
        sleep(0.05)


if __name__ == '__main__':
    data = MyData()
    t1 = Thread(target=producer, args=(data, 20))
    t2 = Thread(target=consumer, args=(data,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()