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

    # Dunder Methods

    def __repr__(self):
         return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
         # return self.first + " " + self.last

    def __str__(self):
        return "Name: " + self.first + " and" + " Last Name: " + self.last

    def __add__(self,other):
        # You can define how objects behave with operators such as +.
        return self.pay + other.pay

    def __len__(self):
        # You can define how objects behave with built-in function like len()
        return len(self.first)


emp_1 = Employee("Lucy","Moritz",500)
emp_2 = Employee("Luky","Eoritz",600)

print(emp_1) # If not specified , it only calls the .__str__() method
print(emp_1.__repr__())
print(emp_1 + emp_2)
print(len(emp_1))




'''
1. In general, the names of special methods take the form of __<name>__, where the two 
underscores preceed and succeed the name. Accordingly, special methods can also be referred 
to as “dunder” (double-underscore) methods.

2.In Python, __repr__ is a special magic (dunder) method used to define an unambiguous, developer-friendly string representation of an object.
Its primary purpose is debugging and logging. Ideally, the string returned by __repr__ 
should look like valid Python code that can be used to recreate the exact same object

3.__str__ is a special magic (dunder) method used to display to the end user 

4.The main concept to remember: Dunder methods let you define how your own objects can behave 
when you use Python's built-in operations(+) and functions (print(), len()) on them.
'''