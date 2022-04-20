# empid attribute of Employee class is made private and is accessible outside the class only using the method getEmpid

class Employee(Person):
    all_employees = EmployeesList()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.__empid = empid
        Employee.all_employees.append(self)
    def getEmpid(self):
        return self.__empid

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class EmployeesList(list):
    def search(self, name):
        matching_employees = []
        for employee in Employee.all_employees:
            if name in employee.fname:
                matching_employees.append(employee.fname)
        return matching_employees
        
e1 = Employee('Jack', 'simmons', 456342)
print(e1.fname, e1.lname)
print(e1.getEmpid())
print(e1.__empid)