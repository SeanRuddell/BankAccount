class BankAccount:
    def __init__(self, account_name, int_rate=0.01, balance=0):
        self.account_name = account_name
        self.int_rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Account type: {self.account_name} Balance: {self.account_balance}")
        return self

    def yield_interest(self):
        self.account_balance *= (self.int_rate + 1)
        return self

savings = BankAccount("Savings")
checking = BankAccount("Checking")

checking.deposit(200).deposit(200).deposit(200).withdraw(100).yield_interest().display_account_info()
savings.deposit(400).deposit(400).withdraw(200).withdraw(100).withdraw(30).withdraw(50).yield_interest().display_account_info()