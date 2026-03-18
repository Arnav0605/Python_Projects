class Student:
    def __init__(self,phy,chem,maths):
        self.phy=phy 
        self.chem=chem 
        self.maths=maths 

    @property
    def CalcPercentage(self):
     return str((self.phy+self.chem+self.maths)/3)+"%"
    
s1=Student(98,99,95)
print(s1.CalcPercentage)
s1.phy=90
print(s1.CalcPercentage)