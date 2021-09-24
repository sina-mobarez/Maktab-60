import os
import pickle


class Person:
    def __init__(self, name, e_mail, gender):
        self.name = name
        self.e_mail = e_mail
        self.gender = gender


class Writer(Person):
    def __init__(self, name, e_mail, gender, genre, code_writing):
        super().__init__(name, e_mail, gender)
        self.genre = genre
        self.code_writing = code_writing

    def __str__(self):
        print(f'name :{self.name} \n E-mail : {self.e_mail} \n Sexuality : {self.gender} \n Genre : {self.genre} \n'
              f'Code-Writing : {self.code_writing}')


class Poet(Person):
    poet_id = 0

    def __init__(self, name, e_mail, gender, style):
        super().__init__(name, e_mail, gender)
        self.style = style
        self.id = Poet.generator_id()

    @classmethod
    def generator_id(cls):
        cls.poet_id += 1
        return cls.poet_id

    def __str__(self):
        print(f'name :{self.name} \n E-mail : {self.e_mail} \n Sexuality : {self.gender} \n Style : {self.style} \n')


class Researcher(Person):
    researcher_id = 1000

    def __init__(self, name, e_mail, gender, field, uni):
        super().__init__(name, e_mail, gender)
        self.field = field
        self.university = uni
        self.id = Researcher.generator_id()

    @classmethod
    def generator_id(cls):
        cls.researcher_id += 1
        return cls.researcher_id

    def __str__(self):
        print(f'name :{self.name} \n E-mail : {self.e_mail} \n Sexuality : {self.gender} \n Field : {self.field} \n'
              f'University : {self.university}')


class Document:
    db = []

    def __init__(self, caption):
        self.caption = caption
        if os.path.isfile('Database.pkl'):
            with open('Database.pkl', 'rb') as reader:
                Document.db = pickle.load(reader)
        self.owners = [item for item in input('enter the owners :').split()]
        if Document.is_valid(self.owners):
            pass
        else:
            print('the Owners entered is not valid')

    @classmethod
    def is_valid(cls, owners):
        if os.path.isfile('Database.pkl'):
            with open('Database.pkl', 'rb') as reader:
                cls.db = pickle.load(reader)
        names = []
        for i in cls.db:
            for value in i.values():
                for value in value.values():
                    for value in value.values():
                        names.append(value)
        counter = 0
        for i in owners:
            if i in names:
                counter += 1
        if counter == len(owners):
            return True
        else:
            return False


class Book(Document):
    def __init__(self, caption, isbn, publications):
        Document.__init__(self, caption)
        self.ISBN = isbn
        self.publications = publications

    def count_owners(self):
        return f'count of owners : {len(self.owners)}'

    def count(self):
        books = []
        for i in Document.db:
            for value in i.values():
                for value in value.values():
                    for value in value.values():
                        books.append(value)

    def __str__(self):
        print(f'Caption :{self.caption} \n Owners : {self.owners} \n ISBN : {self.ISBN} \n'
              f' Publications : {self.publications} \n')


class Poem(Document):
    poem_id = 500

    def __init__(self, caption, literary_mode):
        Document.__init__(self, caption)
        self.literary_mode = literary_mode
        self.id = Poem.generator_id()
        if len(self.owners) > 1:
            print('Poem must have just one owner')

    @classmethod
    def generator_id(cls):
        cls.poem_id += 1
        return cls.poem_id

    def __str__(self):
        print(f'Caption :{self.caption} \n Owners : {self.owners} \n Literary-model : {self.literary_mode} \n')


class Article(Document):
    article_id = 100

    def __init__(self, caption, magazine_name, release_year):
        Document.__init__(self, caption)
        self.magazine_name = magazine_name
        self.release_year = release_year
        self.id = Article.generator_id()

    @classmethod
    def generator_id(cls):
        cls.article_id += 1
        return cls.article_id

    def count_owners(self):
        return f'count of owners : {len(self.owners)}'

    def __str__(self):
        print(f'Caption :{self.caption} \n Owners : {self.owners} \n Magazine-Name : {self.magazine_name} \n'
              f'Release-Year : {self.release_year} \n')


class Database:
    def __init__(self):
        if os.path.isfile('Database.pkl'):
            with open('Database.pkl', 'rb') as reader:
                self.db = pickle.load(reader)
        else:
            self.db = [{'Writer': {},
                        'Poet': {},
                        'Researcher': {}
                        }, {
                           'Book': {},
                           'Poem': {},
                           'Article': {}
                       }]
            with open('Database.pkl', 'wb') as writer:
                pickle.dump(self.db, writer)
        print(self.db)
        books = []
        for i in self.db:
            for value in i.values():
                for key, value in value.items():
                    books.append(value['Book'])
        print(books)

    def add_writer(self, writer):
        writer_db = {
            'Name': writer.name,
            'E-mail': writer.e_mail,
            'Gender': writer.gender,
            'Genre': writer.genre
        }
        self.db[0]['Writer'].update({writer.code_writing: writer_db})
        with open('Database.pkl', 'wb') as writer:
            pickle.dump(self.db, writer)

    def add_poet(self, poet):
        poet_db = {
            'Name': poet.name,
            'E-mail': poet.e_mail,
            'Gender': poet.gender,
            'Style': poet.style
        }
        self.db[0]['Poet'].update({poet.poet_id: poet_db})
        with open('Database.pkl', 'wb') as w:
            pickle.dump(self.db, w)

    def add_researcher(self, researcher):
        researcher_db = {
            'Name': researcher.name,
            'E-mail': researcher.e_mail,
            'Gender': researcher.gender,
            'Field': researcher.field,
            'University': researcher.university
        }
        self.db[0]['Researcher'].update({researcher.researcher_id: researcher_db})
        with open('Database.pkl', 'wb') as w:
            pickle.dump(self.db, w)

    def add_book(self, book):
        book_db = {
            'Caption': book.caption,
            'Owners': book.owners,
            'Publications': book.publications
        }
        self.db[1]['Book'].update({book.ISBN: book_db})
        if book.is_valid(book.owners):
            with open('Database.pkl', 'wb') as w:
                pickle.dump(self.db, w)

    def add_poem(self, poem):
        poem_db = {
            'Caption': poem.caption,
            'Owners': poem.owners,
            'Literary-Model': poem.literary_mode
        }
        self.db[1]['Poem'].update({poem.poem_id: poem_db})
        if len(poem.owners) == 1 and poem.is_valid(poem.owners):
            with open('Database.pkl', 'wb') as w:
                pickle.dump(self.db, w)

    def add_article(self, article):
        article_db = {
            'Caption': article.caption,
            'Owners': article.owners,
            'Magazine-Name': article.magazine_name,
            'Release-Year': article.release_year
        }
        self.db[1]['Article'].update({article.article_id: article_db})
        if article.is_valid(article.owners):
            with open('Database.pkl', 'wb') as w:
                pickle.dump(self.db, w)


# a = Writer('saeed', 'saeed@gmail.com', 'male', 'romance', 12345)
# b = Poet('ali', 'ali.23@gmail.com', 'male', 'ghazal')
# c = Researcher('zahra', 'zahra1@gmail.com', 'female', 'chemistry', 'Tehran')
db = Database()
# db.add_writer(a)
# db.add_poet(b)
# db.add_researcher(c)
# b = Book('math', 'ali saeed hosein', 433, 'jangle')
# db.add_book(b)
# a = Article('hsjs', 'aksks', 202)
# db.add_article(a)
# a = Book('as', 223, 'ssds')
# db.add_book(a)
