from abc import ABC
import datetime

class Customer:
    def __init__(self, customer_id, name, email, phone_number, address, credit_score):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.credit_score = credit_score

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nName: {self.name}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nAddress: {self.address}\nCredit Score: {self.credit_score}"

class Account(ABC):
    lastAccNo = 0

    def __init__(self, account_type, balance, customer):
        Account.lastAccNo += 1
        self.account_number = Account.lastAccNo
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def __str__(self):
        return f"Account Number: {self.account_number}\nCustomer: {self.account_type}\nAccount Type: {self.balance}\nBalance: {self.customer}"

class Transaction:
    def __init__(self, account, description, transaction_type, amount):
        self.account = account
        self.description = description
        self.date_time = datetime.datetime.now()
        self.transaction_type = transaction_type
        self.amount = amount

class SavingsAccount(Account):
   # MINIMUM_BALANCE = 500

    def __init__(self, balance, customer, interest_rate):
        super().__init__("Savings", balance, customer)
        self.interest_rate = interest_rate

class CurrentAccount(Account):
    def __init__(self, balance, customer, overdraft_limit):
        super().__init__("Current", balance, customer)
        self.overdraft_limit = overdraft_limit

class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__("ZeroBalance", 0, customer)