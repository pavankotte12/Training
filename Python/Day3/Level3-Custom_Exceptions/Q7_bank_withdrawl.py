# Custom exception class for a bank account withdrawl
class InsufficientBalanceError(Exception):
    pass

# Function to perform withdrawl
def withdraw(balance,amount):
    
    # Check withdrawl amount greater than balance
    if amount > balance:
        raise InsufficientBalanceError("Withdrawal amount exceeds account balance")
    
    # Return new balance if withdrawl is successful
    return balance - amount

# Successful withdrawl
try:
    balance = withdraw(1000,500)
    print("Withdrawl successful")
    print(f"Available balance {balance}")

except InsufficientBalanceError as e:
    print(e)

# Failed withdrawl
try:
    balance = withdraw(1000,1200)
    print("Withdrawl successful")
    print(f"Available balance {balance}")

except InsufficientBalanceError as e:
    print(f"Error: {e}")

finally:
    print("Done")