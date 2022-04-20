class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
class Employee(Person):
    all_employees = []
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)

p1 = Person('George', 'smith')
print(p1.fname, '-', p1.lname)
e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('John', 'williams', 123656)
print(e1.fname, '-', e1.empid)
print(e2.fname, '-', e2.empid)        

class EmployeesList(list):
    def search(self, name):
        matching_employees = []
        for employee in Employee.all_employees:
            if name in employee.fname:
                matching_employees.append(employee.fname)
        return matching_employees

class Employee1(Person):
    all_employees = EmployeesList()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee1.all_employees.append(self)

e1 = Employee1('Jack', 'simmons', 456342)
e2 = Employee1('George', 'Brown', 656721)
print(Employee1.all_employees.search('or'))        