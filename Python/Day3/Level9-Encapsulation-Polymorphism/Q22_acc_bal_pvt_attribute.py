# Bank Account with deposits, withdrawls and balance with private attribute

# Define BankAccount class
class BankAccount:
    # Constructor to initialize owner and balance
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance    # Private attritube
    
    # Method to deposit money
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited amount {amount}. Current balance : {self.__balance}")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
             print("Withdrawl refused! Insufficient balance.")
        else:
            self.__balance = self.__balance - amount
            print(f"Withdrawl {amount}. Current balance : {self.__balance}")

    # Method to safely return the balance
    def get_balance(self):
        return self.__balance
    
# Create BankAccount object
account = BankAccount("pavan", 5000)

# Perform deposits and withdrawls

account.deposit(3000)
account.withdraw(9000)

# Access current balance
print("Current Balance: ", account.get_balance())