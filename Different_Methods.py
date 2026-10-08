class BankAccount:

    bank_name = "ABC Bank"   # Class variable

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # 1. Instance Method
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} now has ₹{self.balance}")

    # 2. Class Method
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    # 3. Static Method
    @staticmethod
    def is_valid_amount(amount):
        if amount > 0 :
            return True
        else:
            return False

# Creating Instance
account_1 = BankAccount("John",2000)

account_1.deposit(200)
BankAccount.change_bank_name("ABCD")
print(BankAccount.bank_name)
is_valid = BankAccount.is_valid_amount(200)
print(is_valid)

'''
1. Instance methods access the state of a specific object through the self parameter.
2. You create class methods with the @classmethod decorator and use them for operations that involve class-level data / Class Variables
3. You use static methods for utility functionality(repetitive,common chores) that doesn’t need 
class or instance data, and you create them with the @staticmethod decorator. Rule : whenever 
you create a static method, call it using the class name unless you have a specific reason not to.
'''