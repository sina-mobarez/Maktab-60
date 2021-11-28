from datetime import datetime, timedelta


class TravelCard:
    trans_cost = 50  # unit is Dollar $
    used_card = 0

    @classmethod
    def using_of_card(cls):
        cls.used_card += 1


# this card just can use one time
class Throwaway(TravelCard):
    def __init__(self):
        pass

    # method for define using of card per travel
    def using_card(self):
        if self.used_card >= 1:
            print('this card is used before plz buy another')
        elif self.used_card == 0:
            print('enjoy your travel')
            self.using_of_card()

    def __repr__(self):
        return f'This is a throwaway travel card, you can use just on time'


# this card can use by charging it
class CreditCard(TravelCard):
    def __init__(self, first_charge):
        if isinstance(first_charge, int):
            if first_charge < 0:
                print('you can not enter a negative mount for first charge')
                self.charge = 0
            else:
                self.charge = first_charge
        else:
            print('you must enter a integer not strings')
            self.charge = 0

    def using_card(self):
        if self.validate_card:
            TravelCard.using_of_card()
            self.charge -= self.trans_cost

    def recharge(self, mount):
        if isinstance(mount, int):
            if mount < 0:
                print('you can not enter a negative mount for charge')
            else:
                self.charge += mount
        else:
            print('Recharge failed you must enter a integer not strings')

    @property
    def validate_card(self):
        if self.charge < self.trans_cost:
            print('not enough credit please charge your card')
        else:
            return True

    def __repr__(self):
        return f'Credit of card : {self.charge}, count used : {self.used_card}'


# this card is a credit card but has a time to use
class CreditTimingCard(CreditCard):
    def __init__(self, first_charge):
        super().__init__(first_charge)
        self.time_exp = datetime.now() + timedelta(days=180)

    def using_card(self):
        if self.validate_card:
            TravelCard.using_of_card()
            self.charge -= self.trans_cost

    # by every time that you charge your card 30 days add to expiry time
    def recharge(self, mount):
        super().recharge(mount)
        self.time_exp += timedelta(days=30)

    @property
    def validate_card(self):
        if self.charge < self.trans_cost:
            print('not enough credit please charge your card')
        elif self.time_exp < datetime.now():
            print("seems your card is expired ")
        else:
            return True

    def __repr__(self):
        return f'Credit : {self.charge}, count used this card: {self.used_card}, expiry time : {self.time_exp.date()}'



