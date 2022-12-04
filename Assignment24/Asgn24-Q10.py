"""Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values"""

class Employee:

    def __init__(self):
        self.empid = 'EMP18'
        self.name = 'Suresh'
        self.salary = '15 LPA'

    def get_emp(self):
        return self.empid, self.name, self.salary

a = Employee()
print(a.get_emp())