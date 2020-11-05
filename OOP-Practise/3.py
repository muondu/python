from practise1 import Employee
import sqlite3
conn = sqlite3.connect('3.db')
c = conn.cursor()

def create_table(): 
    c.execute('CREATE TABLE IF NOT EXISTS employee(first TEXT,last TEXT, pay INTEGER,email VARCHAR)')
create_table()


emp1 = Employee('Nero','Nesh',10000000,'neronesh2008@gmail.com')
emp2 = Employee('Malli','Muondu',10000000,'mallimuondu@gmail.com')

def insert(emp):
    c.execute('INSERT INTO employee VALUES(?,?,?,?)',(emp.first,emp.last,emp.pay,emp.email))
insert(emp1)




def read():
    c.execute('SELECT * FROM employee')
    print(c.fetchall())
read()