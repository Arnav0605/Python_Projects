class Car:        #Parent class
    @staticmethod
    def start():
        return "Car Started"
    @staticmethod
    def stop():
        return "Car Stopped"
class Toyota(Car):               #Child class
    def __init__(self,name):
        self.name=name
        print(self.name)

car1=Toyota("Camry")
print(car1.start())
car2=Toyota("Fortuner")
print(car2.start())

