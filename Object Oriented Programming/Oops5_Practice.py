class Student:
    def __init__(self,name):
        self.name=name
    def marks(self,marks1,marks2,marks3):
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
        print("Total:",(marks1+marks2+marks3))
    def average(self,total):
        self.total=total
        print("Average is:",(total/3))
s1=Student("Karan")
s1.marks(90,98,89)
s1.average(277)
    
