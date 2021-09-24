class Account:
    minimum_balance = 5000

    def __init__(self, name, balance):
        self.account_name = name
        self.balance = balance

    def receipt(self, amount):
        self.balance += amount
        print(f'Dear {self.account_name} ; Receipt is successful, your stock is {self.balance}')

    def deduce(self, amount):
        if Account.validation(amount, self.balance):
            self.balance -= amount
            print(f'Dear {self.account_name} ; Deduce is successful, your stock is {self.balance}')
        else:
            print(f'Dear {self.account_name} ; your stock is too less for this deduce')

    def transfer(self, account, amount):
        if Account.validation(amount, self.balance):
            account.receipt(amount)
            self.balance -= amount
            print(f'Dear {self.account_name} ; Transfer is successful, your stock is {self.balance}')
        else:
            print(f'Dear {self.account_name} ; your stock is too less for this deduce')

    @classmethod
    def validation(cls, amount, balance):
        if (balance - amount) < cls.minimum_balance:
            return False
        else:
            return True

    @property
    def show_balance(self):
        return f'Dear {self.account_name} ; your Balance is {self.balance}'



