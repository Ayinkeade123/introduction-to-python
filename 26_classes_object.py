#Create a Python class called BankAccount
#That represents a bank account with attributes for the account holder's name, balance, and account number.
#Add validation to ensure the balance cannot go below zero

class BankAccount:
    def __init__(self,account_name,account_number, account_balance=0):
        self.account_name = account_name
        self.account_number = account_number
        self.account_balance = account_balance
        
#Implement methods for deposit, withdraw, and check_balance.
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposit successful! New balance:{self.account_balance:}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                print(f"Withdrawal successful! New balance: {self.account_balance:}")
            else:
                 print("Insufficient funds. Withdrawal declined.")
        else:           
            print("Withdrawal amount must be positive.")

def check_balance(self):
        print(f"Account balance: {self.account_balance}")


# Create a new bank account
account = BankAccount("zainab", "3055899340", 1000)

# Deposit money
account.deposit(500)  # Output: Deposit successful. New balance: 1500

# Withdraw money
account.withdraw(300)  # Output: Withdrawal successful. New balance: 1200

# Attempt to withdraw more than the balance
account.withdraw(1300)  # Output: Insufficient funds. Withdrawal declined.

# Check balance
account.check_balance()  # Output: Account balance: 1200