import os
import pickle
from datetime import timedelta, datetime

from bank_db_table import connect


class Account:
    minimum_balance = 5000

    # create a pickle file for store data
    def __init__(self, name, balance):
        self.account_name = name
        self.balance = balance
        cursor = connect.cursor()
        insert = " INSERT INTO account (name, balance) VALUES (%s, %s);"
        item = (self.account_name, self.balance)
        cursor.execute(insert, item)
        connect.commit()
        cursor.close()
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

        # postgres db operate
        cursor = connect.cursor()
        cursor.execute("SELECT account_id FROM account WHERE name = %s;", (self.account_name,))
        connect.commit()
        account = cursor.fetchone()
        insert = " INSERT INTO history (account_id, history_time, action, amount) VALUES (%s, %s, %s, %s);"
        item = (account, self.time, "receipt", amount)
        cursor.execute(insert, item)
        connect.commit()
        insert = " UPDATE account SET balance = %s WHERE account_id = %s;"
        item = (self.balance, account)
        cursor.execute(insert, item)
        connect.commit()
        cursor.close()

        self.history.append(f'{self.account_name} receipt +{amount} >>> {self.time}')
        self.db.append({self.time: {"receipt": f'+{amount}'}})
        print(f'Dear {self.account_name} ; Receipt is successful, your stock is {self.balance}')

    # define a method for save deduce
    def deduce(self, amount):
        t = datetime.now()
        self.time = t.strftime("%Y-%b-%d %X")
        if Account.validation(amount, self.balance):
            self.balance -= amount

            # postgres db operate
            cursor = connect.cursor()
            cursor.execute("SELECT account_id FROM account WHERE name = %s;", (self.account_name,))
            connect.commit()
            account = cursor.fetchone()
            insert = " INSERT INTO history (account_id, history_time, action, amount) VALUES (%s, %s, %s, %s);"
            item = (account, self.time, "deduce", amount)
            cursor.execute(insert, item)
            connect.commit()
            insert = " UPDATE account SET balance = %s WHERE account_id = %s;"
            item = (self.balance, account)
            cursor.execute(insert, item)
            connect.commit()
            cursor.close()

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

            # postgres db operate
            cursor = connect.cursor()
            cursor.execute("SELECT account_id FROM account WHERE name = %s;", (self.account_name,))
            connect.commit()
            first_account = cursor.fetchone()
            insert = " INSERT INTO history (account_id, history_time, action, amount) VALUES (%s, %s, %s, %s);"
            item = (first_account, self.time, "transfer", amount)
            cursor.execute(insert, item)
            connect.commit()
            insert = " UPDATE account SET balance = %s WHERE account_id = %s;"
            item = (self.balance, first_account)
            cursor.execute(insert, item)
            connect.commit()
            cursor.close()

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
            te = time_end.strftime("%Y-%b-%d %X")
            ts = time_start.strftime("%Y-%b-%d %X")

            # postgres time show
            cursor = connect.cursor()
            cursor.execute("SELECT account_id FROM account WHERE name = %s;", (self.account_name,))
            connect.commit()
            account = cursor.fetchone()
            cursor.execute("SELECT * FROM history\
                           WHERE account_id = %s and history_time > %s \
                           and history_time < %s;",
                           (account, ts, te))
            connect.commit()
            hiss = cursor.fetchall()
            print(hiss)
            cursor.close()
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

Account.history(a, "2021-11-06 17:08")
