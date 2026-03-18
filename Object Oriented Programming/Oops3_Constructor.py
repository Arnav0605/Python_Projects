class Student:
     def __init__(self,fullname,marks):
        self.name = fullname
        self.marks=marks
        print("Adding new student in database")     #object attribute(precedence) > class attribute(precedence)

s1=Student("karan",89)
print(s1.name,s1.marks)
s2=Student("hari",99)
print(s2.name,s2.marks)  

   