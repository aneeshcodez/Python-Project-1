
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
