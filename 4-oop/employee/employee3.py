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

emp = []

while 1:
    comm = raw_input("Enter 1 to add employee, 2 to list employees: ")
    if comm == "1":
        name = raw_input("Enter Name: ")
        salary = input("Enter salary: ")
        title = raw_input("Enter title: clerk or manager: ")
        emp.append(Employee(name,salary,title))
    elif comm == "2":
        try:
            for i in range(0,len(emp)):
                emp[i].displayEmployee()
            print "Total Employee %d, Total Manager %d, Total Clerk %d" % (Employee.empCount, Employee.manCount, Employee.clerkCount)
        except IndexError:
            print "No current employees"
    else:
        print "Invalid input"
