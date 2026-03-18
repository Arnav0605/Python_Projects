class Car:             #Parent Class
    @staticmethod
    def start():
        return "Car Started"
    @staticmethod
    def stop():
        return "Car Stopped"
    
class Toyota(Car):            #Child Class
    def __init__(self,name):
        self.name=name
        print(self.name)

class Fortuner(Toyota):       #Child Class
    def __init__(self,type):
        self.type=type
        print(self.type)

car1=Fortuner("diesel")
print(car1.start())
