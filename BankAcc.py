class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")
    def balance(self):
        return self.balance
    
# Create a new bank account
account = BankAccount("John Doe")

print("Depositing funds...")
account.deposit(1000)

print(account.balance())
