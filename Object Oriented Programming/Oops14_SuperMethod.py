class Car():
    def __init__ (self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car Started")
    @staticmethod
    def stop():
        print("Car Stoped")

class ToyotaCar(Car):
    def __init__ (self,name,type):
        self.name=name
        super().__init__(type)     #super() method used to use methods of parent class
        super().start()            #super() method used to use methods of parent class

car1=ToyotaCar("Petrol","Camry")
print(car1.type)


