# Polymorphism Example
#In the below shown example, you will find

#Improvised Employee class with two methods getSalary and getBonus.

#Definition of ContractEmployee class derived from Employee. It overrides functionality of getSalary and getBonus methods found in it's parent class Empl

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

class Employee(Person):
    all_employees = EmployeesList ()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)
    def getSalary(self):
        return 'You get Monthly salary.'
    def getBonus(self):
        return 'You are eligible for Bonus.'