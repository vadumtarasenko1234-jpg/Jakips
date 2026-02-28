import random

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # публічний атрибут
        self.__balance = balance  # приватний атрибут

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance

account = BankAccount("Bohdan", 1000)
account.deposit(500)
print(account.get_balance())  # 1500
for _ in range(5):
    amount = random.randint(100, 500)
    account.deposit(amount)
    print(f"Deposited: {amount}, Balance: {account.get_balance()}")

for _ in range(3):
    amount = random.randint(100, 300)
    result = account.withdraw(amount)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Withdrew: {result}, Balance: {account.get_balance()}")