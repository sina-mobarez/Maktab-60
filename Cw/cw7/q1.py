import os
import pickle


class Address:
    def __init__(self, st, city):
        self.st = st
        self.city = city

    def __str__(self):
        return f'Street: {self.st}, City: {self.city}'


class Person:
    def __init__(self, name, email, ph_num):
        self.name = name
        self.email = email
        self.ph_num = ph_num

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Phone Number: {self.ph_num}'


class Contact(Address, Person):
    def __init__(self, st, city, name, email, ph_num):
        self.obj_Address = Address(st, city)
        self.obj_person = Person(name, email, ph_num)


class PhoneBook(Contact):
    def __init__(self, st, city, name, email, ph_num):
        super().__init__(st, city, name, email, ph_num)
        if os.path.isfile('phonebook.pkl'):
            with open('phonebook.pkl', 'rb') as reader:
                self.phone_book = pickle.load(reader)
        else:
            self.phone_book = []
            with open('phonebook.pkl', 'wb') as writer:
                pickle.dump(self.phone_book, writer)

    def add_contact(self):
        contact_dic = {
            'Name': self.obj_person.name,
            'E-mail': self.obj_person.email,
            'Phone_num': self.obj_person.ph_num,
            'Street': self.obj_Address.st,
            'City': self.obj_Address.city
        }
        self.phone_book.append(contact_dic)
        with open('phonebook.pkl', 'wb') as f:
            pickle.dump(self.phone_book, f)

    def __str__(self):
        return f'Name : {self.phone_book[-1]["Name"]} \nPhone_number: {self.phone_book[-1]["Phone_num"]} \nAddress :' \
               f'{self.phone_book[-1]["Street"]}_{self.phone_book[-1]["City"]}'

    def search(self):
        f = input('enter yr name:')
        counter = 0
        for i in self.phone_book:
            if i["Name"] == f:
                print(i)
                counter += 1
        if counter == 0:
            print('Not find')


c = PhoneBook('adli', 'esfahan', 'ali', 'shujs', 987)
c.add_contact()
print(c)
c.search()
