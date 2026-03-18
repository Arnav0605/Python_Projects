class Car:
    def __init__(self):
        self.acc=False       #These Methods or Functions are hidden
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("Car Started")      

car1=Car()
car1.start()
