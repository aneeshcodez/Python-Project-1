class Employee:

    # Class Variable
    raise_amount = 1.04

    # To Calc no of Employee
    no_of_employees = 0

    def __init__(self,first,last,pay):
        # Instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + "gmail.com"
        Employee.no_of_employees = Employee.no_of_employees + 1


    # Method 1
    def emp_full_name(self):
        return self.first + " " + self.last

    # Method 2
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Lucy","Moritz",5000)
emp_2 = Employee("Suresh","Raina",6000)

# Concept : We can do this if we wanted to raise a particular amount only for a particular employee
# and we do not want to use the common Raise Amount(1.04)
emp_1.raise_amount = 1.06

print(emp_1.pay) # o/p : 5000
emp_1.apply_raise()
print(emp_1.pay) # o/p : 5300 since now we have called the Raise function

print(Employee.no_of_employees)

# 3.29

'''
1. Class Variables are variables that are shared among all instances of a Class

'''
