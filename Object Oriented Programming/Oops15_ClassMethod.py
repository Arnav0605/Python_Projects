class Person:
    name="anonymous"
    @classmethod
    def ChangeName(cls,name):      #Now we can change the name for every object we create
        cls.name=name

p1=Person()
p1.ChangeName("Karan")
print(p1.name)
print(Person.name)
