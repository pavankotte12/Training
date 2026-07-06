# Bank Account with deposits, withdrawls and available balance

# Define BankAccount class
class BankAccount:
    # Constructor to initialize owner and balance
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount {amount}. Current balance : {self.balance}")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
             print("Withdrawl refused! Insufficient balance.")
        else:
            self.balance = self.balance - amount
            print(f"Withdrawl {amount}. Current balance : {self.balance}")

# Create BankAccount object
account = BankAccount("pavan")

# Perform deposits and withdrawls
account.deposit(5000)
account.withdraw(1000)
account.deposit(3000)
account.withdraw(8000)
