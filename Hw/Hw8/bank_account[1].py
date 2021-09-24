import os
import pickle
from datetime import timedelta, datetime


class Account:
    minimum_balance = 5000

    # create a pickle file for store data
    def __init__(self, name, balance):
        self.account_name = name
        self.balance = balance
        if os.path.isfile('History.pkl'):
            with open('History.pkl', 'rb') as reader:
                self.history = pickle.load(reader)
                self.db = pickle.load(reader)
        else:
            self.history = []
            self.db = []
            with open('History.pkl', 'wb') as writer:
                pickle.dump(self.history, writer)
                pickle.dump(self.db, writer)

    # define a method for save receipt
    def receipt(self, amount):
        t = datetime.now()
        self.time = t.strftime("%Y-%b-%d %X")
        self.balance += amount
        self.history.append(f'{self.account_name} receipt +{amount} >>> {self.time}')
        self.db.append({self.time: {"receipt": f'+{amount}'}})
        print(f'Dear {self.account_name} ; Receipt is successful, your stock is {self.balance}')

    # define a method for save deduce
    def deduce(self, amount):
        t = datetime.now()
        self.time = t.strftime("%Y-%b-%d %X")
        if Account.validation(amount, self.balance):
            self.balance -= amount
            self.history.append(f'{self.account_name} deduce -{amount} >>> {self.time}')
            self.db.append({self.time: {"deduce": f'-{amount}'}})

            print(f'Dear {self.account_name} ; Deduce is successful, your stock is {self.balance}')
        else:
            print(f'Dear {self.account_name} ; your stock is too less for this deduce')

    # define a method for save transfer
    def transfer(self, account, amount):
        t = datetime.now()
        self.time = t.strftime("%Y-%b-%d %X")
        if Account.validation(amount, self.balance):
            account.receipt(amount)
            self.balance -= amount
            self.history.append(f'{self.account_name} transfer -{amount} >>> {self.time}')
            self.db.append({self.time: {"transfer": f'-{amount}'}})

            print(f'Dear {self.account_name} ; Transfer is successful, your stock is {self.balance}')
        else:
            print(f'Dear {self.account_name} ; your stock is too less for this deduce')

    # define a class method for validation of any money movement
    @classmethod
    def validation(cls, amount, balance):
        if (balance - amount) < cls.minimum_balance:
            return False
        else:
            return True

    @property
    def show_balance(self):
        return f'Dear {self.account_name} ; your Balance is {self.balance}'

    # get a time in given format and check it
    # yyyy-mm-dd hh:mm
    def history(self, date_time):
        his = []
        try:
            time2 = str(date_time)
            time_loc = datetime.strptime(time2, "%Y-%m-%d %H:%M")
            print(f'your all history >> {self.history}')
            time_end = time_loc + timedelta(minutes=2)
            time_start = time_loc + timedelta(minutes=-2)
            for item in self.db:
                for i in item:
                    tt = datetime.strptime(i, "%Y-%b-%d %X")
                    if tt >= time_start and tt <= time_end:
                        his.append(item)
        except ValueError:
            print('your entered time is wrong')
        finally:
            if len(his) != 0:
                print(f'your history you want : /n {his}')
            else:
                print('there is no data for show in this time')


a = Account('sina', 22)
b = Account('jamal', 120500)

a.receipt(1200)
a.transfer(b, 4200)
print(b.show_balance)

b.transfer(a, 1230000)
b.transfer(a, 110000)
print(a.show_balance)
Account.history(a, "2021-9-21 20:15")
