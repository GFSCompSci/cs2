#!/usr/bin/python

class Employee:
    'Common base class for all employees'
    empCount = 0
    manCount = 0
    clerkCount = 0

    def __init__(self, name, salary, title):
        self.name = name
        self.salary = salary
        self.title = title
        Employee.empCount += 1
        if self.title == "manager":
            Employee.manCount += 1
        if self.title == "clerk":
            Employee.clerkCount +=1



    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary,  ", Title: ", self.title

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000, "manager")
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000, "clerk")
emp3 = Employee("Eric", 3000, "clerk")

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()


print "Total Employee %d" % Employee.empCount
print "Total Manager %d" % Employee.manCount
print "Total Clerk %d" % Employee.clerkCount
