import sqlite3
import time
import datetime
import random
conn = sqlite3.connect('5.db')
c = conn.cursor()

def create_table():
#    c.execute('CREATE TABLE IF NOT EXISTS name_age(name1 TEXT, name2 TEXT, age INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS name(name1 TEXT)')
    
create_table()

def update_db():
    while True:
        name1 = input("Enter your name:  ")
#        name2 = str(input("Enter your second name: "))
#        age = int(input("Enter your age: "))
        if not name1.isalpha():
            continue
        else:
            c.execute("INSERT INTO name(name1) VALUES(?)",(name1,))
            conn.commit()
            print("Prossed nicely. Fun fact. Hard core minecraft is in java eddition")
            break

update_db()  


    
def read_from_db():
    c.execute('SELECT * FROM name')
    data = c.fetchall()
    print(data)
#    for row in data:
#        print(row)
    
#    time.sleep(1)
read_from_db()
#   c.close()
#conn.close()