class BankAccount (object):
    interest_rate = 0.05 #class variable <interest_rate>
    def __init__(self, name, number, balance):
        self.name = name #instance variable <self.name>
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Withdrawal amount exceeds balance")
        else:
            self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def apply_fees(self):
        self.balance = self.balance - 5
