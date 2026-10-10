class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Single underscore signals an internal/protected attribute

    # The Getter
    @property
    def salary(self):
        return self._salary

    # The Setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value


emp = Employee("Alice", 50000)

# Accessing like a normal attribute triggers the getter
print(emp.salary)

# Assigning like a normal attribute triggers the setter
emp.salary = 60000

print(emp.salary)


# This will raise a ValueError
# emp.salary = -1000


'''
1.SINGLE LEADING UNDERSCORE : 
Naming an attribute in your class self._var1 indicates to the user of the class that the 
attribute should only be accessed by the class's internals (or perhaps those of a subclass) 
and that they need not directly access it and probably shouldn't modify it. 
You should use leading underscores in the same places that you would use a private or 
protected field in Java or C#, but be aware that the language doesn't actually enforce 
non-access - instead you trust your class's user to not do anything stupid, and 
leave them the option of accessing (or modifying) your class's private field 
if they're really, really sure that they know what they're doing and it makes sense.

2.In Python, getters and setters are used to manage access to an object's internal data, 
ensuring encapsulation(protection of data) and validation

3.The @property decorator in Python is a built-in feature that allows you to turn a class 
method into a "managed attribute". This means you can access, set, or delete data using 
clean dot notation (like obj.variable) while running custom logic, validation, 
or dynamic computations behind the scenes.

The @property decorator allows you to define methods that can be accessed exactly like 
normal attributes. This keeps your syntax clean while allowing you to add 
logic (like data validation) behind the scenes

4.
Why @property for the getter?
@property tells Python to treat the salary() method like an attribute.
So you can write emp.salary instead of emp.salary().

Why @salary.setter for the setter?
@salary.setter tells Python: "Add the setter behavior to the salary property we already created."
So when you write emp.salary = 50000, Python calls the setter.

Why not use @property for both?
Because @property creates a new property, whereas @salary.setter specifically adds setter behavior to the existing salary property.



"Why do I need a getter? I can already write emp1.salary and get the salary."
Excellent question! but Our problem: We want to control what happens when someone reads, changes, or deletes an employee's salary.
You are right. We don't need a getter just to read a normal variable. 
*A getter becomes useful when we want to control what happens when someone reads an attribute, 
without changing how they access it.

*Same way A setter lets us control what happens when someone assigns a new value to a 
property without changing how they access it.


'''