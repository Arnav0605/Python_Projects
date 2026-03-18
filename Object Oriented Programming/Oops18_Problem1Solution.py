import math
class Circle():
    def __init__(self,r):
        self.r=r

    def Area(self):
        return math.pi*self.r*self.r
    def Perimeter(self):
        return 2*math.pi*self.r
    
circle1=Circle(5)
print("The Area is:",circle1.Area())
print("ThePerimeter is:",circle1.Perimeter())
    
    

