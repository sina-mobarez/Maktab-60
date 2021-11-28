from datetime import datetime
import redis
import random
import csv  # for create a log file

redis_client = redis.Redis(charset="utf-8", decode_responses=True)


class WrongUsernameOrPass(Exception):
    pass


class UsernameAlreadyTaken(Exception):
    pass


class NotEnoughCapacity(Exception):
    pass


# only Admin can Use this class and methods
class Event:
    event_id = random.randint(1200, 20000)

    # date_time of event must be in this format : "yyyy-mm-dd hh:mm"
    def __init__(self, date_time, location, capacity, price_ticket):
        self.date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        self.location = location
        self.capacity = capacity
        self.left_capacity = capacity
        self.price_ticket = price_ticket
        self.id = Event.generator_id()

    @property
    def save(self):
        dt = str(self.date_time)
        redis_client.hset(
            f'Event:{self.id}:Info', mapping=
            {
                "Location": self.location,
                "Date and Time": dt,
                "Capacity": self.capacity,
                "Price of Ticket": self.price_ticket,
                "Left Capacity": self.left_capacity,
                "Event id": self.id
            }
        )

    # you can set discount code by amount of discount; ...like ---> 20%
    def add_discount_code(self, percent, *args):
        for i in args:
            redis_client.lpush(f'discount:{percent}', i)

    def show_sold_ticket(self, event_id):
        cap = redis_client.hget(f'Event:{event_id}:Info', "Capacity")
        left_cap = redis_client.hget(f'Event:{event_id}:Info', "Left Capacity")
        sold_tic = int(cap) - int(left_cap)
        return f'for this Event {event_id} ; sold ticket : {sold_tic} >>> left ticket : {left_cap}'

    @classmethod
    def generator_id(cls):
        cls.event_id += 1
        return cls.event_id


# username : Admin ; password : Admin >>> for admin permission
class SignUp:
    def __init__(self, username, password, phone_number):
        self.user_name = username
        self.password = password
        self.phone_number = phone_number

    def submit(self):
        if self.user_name in redis_client.keys(self.user_name):
            raise UsernameAlreadyTAken
        else:
            redis_client.hset(self.user_name,
                              mapping={'password': self.password, 'phone_number': self.phone_number}
                              )


# by this method you must first login in system and then can operate another thing
class LoginUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def checking(self):
        if 'Admin' in redis_client.keys(str(self.username)):
            if 'Admin' == redis_client.hget(str(self.username), 'password'):
                return f'Admin'
        elif str(self.username) in redis_client.keys(str(self.username)):
            if str(self.password) == redis_client.hget(str(self.username), 'password'):
                return True
            else:
                raise WrongUsernameOrPass

        else:
            raise WrongUsernameOrPass

    @property
    def show_event(self):
        for event in redis_client.keys('Event*'):
            print(redis_client.hgetall(event))

    def choose_event(self, event_id, num_of_ticket, discount='None'):
        price = redis_client.hget(f'Event:{event_id}:Info', "Price of Ticket")
        if int(num_of_ticket) > redis_client.hget(f'Event:{event_id}:Info', "Left Capacity"):
            raise NotEnoughCapacity
        reduction = 1
        for code in redis_client.keys('discount*'):
            if discount in redis_client.lrange(code, 0, -1):
                reduction = int(code[8:10])
        if reduction == 1:
            self.final_price = int(price) * int(num_of_ticket)
        else:
            self.final_price = (int(price) * int(num_of_ticket)) - ((int(price) / 100) * reduction)
        return f'for Event {event_id}, {num_of_ticket} tickets are reserved ; you must pay : {self.final_price}'

    # just call this method and pay is done
    def payment(self, event_id, number_ticket):
        l_cap = redis_client.hget(f'Event:{event_id}:Info', "Left Capacity")
        capacity = int(l_cap) - number_ticket
        redis_client.hset(f'Event:{event_id}:Info', mapping={"Left Capacity": capacity})
        return f'Your ticket is ready -->count : {number_ticket} '


# let's create a csv file for store logs
headers = ('Date-Time', 'Status', 'Type', 'Info')
with open('logs.csv', 'w+', newline='') as log:
    writer = csv.DictWriter(log, fieldnames=headers)
    writer.writeheader()


# define a plan for run one by one of classes
def system():
    while True:
        print('Hello and welcome to CelebrateShop')
        operate = input('if you have an account enter "Y" : \n if not; enter "S" :')
        if operate == 'Y':
            user = input('enter your UserName :')
            pas = input('enter your PassWord :')
            account = LoginUser(user, pas)
            try:
                if account.checking():
                    account.show_event
                    event = input("Choose an Event and enter event's ID:")
                    ticket = input("Enter number of ticket :")
                    discount_code = input("If you have discount code enter it : ")
                    print(account.choose_event(event, ticket, discount_code))
                    confirm = input("If you want to pay please enter exactly 'Y' : ")
                    if confirm == 'Y':
                        try:
                            print(account.payment(event, ticket))
                        except NotEnoughCapacity:
                            print('Not enough capacity ')
                            inf = [str(datetime.now()), 'Failed', 'Error', 'not enough capacity']
                            with open('logs.csv', 'a') as w:
                                c = csv.writer(w)
                                c.writerow(inf)
                                w.close()
                    inf = [str(datetime.now()), 'Success', 'Purchase', 'selling ticket']
                    with open('logs.csv', 'a') as w:
                        c = csv.writer(w)
                        c.writerow(inf)
                        w.close()
                elif account.checking() == 'Admin':
                    ad = input('for create an event enter "E" : ')
                    if ad == "E":
                        dt = input('Enter date and time of event beginning in this format : >> yyyy-mm-dd hh:mm << : ')
                        loc = input('Enter location of event : ')
                        cap = input('Enter capacity of event : ')
                        pr = input('Enter price of ticket"s event : ')
                        ev = Event(dt, loc, cap, pr)
                        sv = input('are sure to create this event : /enter Y : ')
                        if sv == 'Y':
                            ev.save
                            # logs
                            inf = [str(datetime.now()), 'Success', 'Operation', 'Create a new event']
                            with open('logs.csv', 'a') as w:
                                c = csv.writer(w)
                                c.writerow(inf)
                                w.close()
                        dis = input('Do you want to put discount code : /enter Y :')
                        if dis == 'Y':
                            per = input('Enter how much to discount : /in percent like 20% : ')
                            co = input('Enter your codes : ').split()
                            ev.add_discount_code(pre, co)
                        watch = input('Do you want to see sold ticket of an event : /enter Y :')
                        if watch == 'Y':
                            id_ev = input('enter id of event : ')
                            print(ev.show_sold_ticket(id_ev))

            except WrongUsernameOrPass:
                print('UserName or Password is wrong! ')
                inf = [str(datetime.now()), 'Failed', 'Error', 'enter a wrong user or pass']
                with open('logs.csv', 'a') as w:
                    c = csv.writer(w)
                    c.writerow(inf)
                    w.close()
            except Exception:
                print('Something go wrong! ')
                inf = [str(datetime.now()), 'Failed', 'Error', 'something wrong']
                with open('logs.csv', 'a') as w:
                    c = csv.writer(w)
                    c.writerow(inf)
                    w.close()
            break
        elif operate == 'S':
            u = input('enter your User name : ')
            p = input('enter your password : ')
            phone = input('enter your phone number : ')
            sig = SignUp(u, p, phone)
            try:
                sig.submit()
            except UsernameAlreadyTAken:
                print('username already taken !')
                inf = [str(datetime.now()), 'Failed', 'Error', 'enter a taken username']
                with open('logs.csv', 'a') as w:
                    c = csv.writer(w)
                    c.writerow(inf)
                    w.close()
            break


# for set admin account
redis_client.set('Admin', 'Admin')
run = system()
