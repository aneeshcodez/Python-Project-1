
class InsufficientBalanceError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    pass


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance in your account")

        self.balance -= amount
        print(f"Withdrawal successful. Remaining balance: ₹{self.balance}")


account = BankAccount("Aneesh", 1000)

try:
    amount = float(input("Enter withdrawal amount: "))
    account.withdraw(amount)

except ValueError as error:
    print("Invalid input:", error)

except InsufficientBalanceError as error:
    print("Transaction failed:", error)

print("Program execution completed.")

'''
When a class inherits from Exception class, you can pass your error message directly 
as an argument when raising it (raise MyError("Message")), and Python will automatically 
store that message and display it whenever the error is caught, printed, or 
left unhandled in the terminal.

'''
