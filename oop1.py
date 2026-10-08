class Employee:
    def __init__(self,first,last,pay):
        # Instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + "gmail.com"

    # Method
    def emp_full_name(self):
        return self.first + " " + self.last


emp_1 = Employee("Lucy","Moritz",500)
emp_2 = Employee("Luky","Eoritz",500)

print(emp_1)
print(emp_2)

print(emp_1.pay)
print(emp_2.pay)

emp2_full_name = emp_2.emp_full_name()
print(emp2_full_name)

# Concept : Both these lines do exactly the same thing . And Actually the first line gets
# transformed into as 2nd line Behind the Scene
emp_1.emp_full_name()
print(Employee.emp_full_name(emp_1))

'''
1. Here 'self' is emp_1 / emp_2 i.e Employee object
2. emp_1 / emp_2 is called as an Instance 
3. Instance variables is used for Data that is Unique to each Instance. Here In this program ,It is set using 'self' argument
'''



# Read the Docs for this Class
# Instance variable