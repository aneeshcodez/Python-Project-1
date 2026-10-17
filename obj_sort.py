class Employee:
    def __init__(self, name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},{})'.format(self.name,self.age,self.salary)

emp_1 = Employee('Aohn',22,5000)
emp_2 = Employee('Bmith',23,6000)
emp_3 = Employee('Michael',24,7000)

employees = [emp_1,emp_2,emp_3]

# def sort_employees(emp):
#     return emp.name

s_employees = sorted(employees, key=lambda emp:emp.age)
for emp in s_employees:
    print(emp)