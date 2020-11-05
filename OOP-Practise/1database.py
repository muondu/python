from homework1 import employee
import sqlite3
conn = sqlite3.connect('1.db')
c = conn.cursor()

def create_table(): 
    c.execute('CREATE TABLE IF NOT EXISTS employee(name TEXT, pay INTEGER)')
create_table()

emp1 = employee('Nesh',10000000,)
emp2 = employee('Malli',10000000)

def insert(emp):
    c.execute('INSERT INTO employee VALUES(?,?)',(emp.name,emp.pay))
insert(emp1)




def read():
    c.execute('SELECT * FROM employee')
    print(c.fetchall())
read()
