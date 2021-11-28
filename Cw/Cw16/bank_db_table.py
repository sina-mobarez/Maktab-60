from psycopg2 import *

connect = connect(database="bank", user="postgres",
                  password="QWT67P53", host="127.0.0.1", port="5432")
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS account
                      (account_id serial PRIMARY KEY NOT NULL,
                       name VARCHAR(50) NOT NULL,
                       balance INT NOT NULL
                       );''')
connect.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS history
                      (history_id serial PRIMARY KEY NOT NULL,
                       account_id INT NOT NULL,
                       history_time TIMESTAMP NOT NULL,
                       action VARCHAR(50) NOT NULL,
                       amount INT NOT NULL,
                       FOREIGN KEY(account_id)
                              REFERENCES account(account_id));''')
connect.commit()
