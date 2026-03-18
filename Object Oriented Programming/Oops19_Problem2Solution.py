class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showdetails(self):
        print("Role:",self.role,"\nDepartment:",self.department,"\nSalary:",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Hello:",self.name)
        super().__init__("Developer","IT","Rs.5000000")

Emp1=Engineer("Aman",30)
Emp1.showdetails()