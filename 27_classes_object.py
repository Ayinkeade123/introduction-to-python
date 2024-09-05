class BankAccount:
    def __init__(self, account_holder_name, account_number, initial_balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal successful. New balance: {self.balance}")
            else:
                print("Insufficient funds. Withdrawal declined.")
        else:
            print("Withdrawal amount must be positive.")
    
    def check_balance(self):
        print(f"Account balance: {self.balance}")

# Create a new bank account
account = BankAccount("John Doe", "123456789", 100)

# Deposit money
account.deposit(50)  # Output: Deposit successful. New balance: 150

# Withdraw money
account.withdraw(30)  # Output: Withdrawal successful. New balance: 120

# Attempt to withdraw more than the balance
account.withdraw(200)  # Output: Insufficient funds. Withdrawal declined.

# Check balance
account.check_balance()  # Output: Account balance: 120