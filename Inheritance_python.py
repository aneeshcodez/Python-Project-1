class Employee:

    # Class Variable
    raise_amount = 1.04

    # Constructor
    def __init__(self,first,last,pay):
        # Instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + "gmail.com"

    # Method
    def emp_full_name(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Inheriting Class
class Developer(Employee):

    raise_amount = 2.5

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first, last, pay) # Employee.__init__(self,first, last, pay)
        # also produces the same result # We are also avoiding DRY here
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
            self.employees.append(emp)

    def remove_emp(self,emp):
            self.employees.remove(emp)

    def print_emp(self):
            for emp in self.employees:
                print(emp.emp_full_name())
                '''
                self.employees is a list, but the elements inside that list are still objects.
                Here, The list contains the dev_1 object.
                dev_1 is an object of the Developer class. Developer inherits from Employee, so dev_1 can access the emp_full_name() method defined in Employee.
                '''
            # print(self.employees)


emp_1 = Employee("Suresh","Raina",500)
emp_2 = Employee("Virat","Kohli",500)

dev_1 = Developer("Ram","Sam","400","python")

manager_1 = Manager("Ramesh","Ragu",2000,[dev_1])
manager_1.print_emp()

# print(emp_1.first) # o/p : Suresh

# print(help(Developer))
# o/p :
# Method resolution order:
#  |      Developer
#  |      Employee
#  |      builtins.object

# print(dev_1.prog_lang)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


'''
1. super(): Python handles passing the current instance('self') to the parent's method.Thats why 
we didnt specify it along with other parameters in the above program.
super() doesn't simply mean "call the parent class." More precisely, it follows Python's 
method resolution order (MRO) to find the next class's implementation.
'''


