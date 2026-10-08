class Employee:
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


# Inheriting Class
class Developer(Employee):

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first, last, pay) # Employee.__init__(self,first, last, pay)
        # also produces the same result # We are also avoiding DRY here
        self.prog_lang = prog_lang


emp_1 = Employee("Suresh","Raina",500) # It will produce same result as 'emp_1 = Employee("Lucy","Moritz",500)'
emp_2 = Employee("Virat","Kohli",500)

dev_1 = Developer("Ram","Sam","400","python")

print(emp_1.first) # o/p : Suresh

# print(help(Developer))
# o/p :
# Method resolution order:
#  |      Developer
#  |      Employee
#  |      builtins.object

print(dev_1.prog_lang)


