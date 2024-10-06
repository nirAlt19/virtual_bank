from enum import Enum


class AccountType(Enum):
    CHECKING = 1
    SAVINGS = 2


class BankAccount:
    def __init__(self, account_number, owner, account_type, balance, transactions):
        self.account_number = account_number #todo: Account number == UUID?
        self.owner = owner #    todo: Should this be the user_id? We forced unique email but still...
        self.account_type = account_type
        self.balance = balance
        self.transactions = transactions

    def deposit(self, amount):
        self.balance += amount #    todo: Will i use methods or everything will be used from the API? How will the components communicate?

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
