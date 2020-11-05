import sqlite3
conn = sqlite3.connect('2.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS name_age(name TEXT, age INTEGER)')
    
create_table()

def update_db():
    while True: 
        name1 = str(input("Enter your name: "))
        if not name1.isalpha():
            continue 
        else:
            try:
                age = int(input("Enter your age: "))
            except ValueError:
                print("I did not understand you")
        c.execute("INSERT INTO name_age(name, age)VALUES(?,?)",(name1, age))
        conn.commit()
        print("Yahoo. It is done")
        break
    
    
update_db()
def read_db():
    c.execute('SELECT * FROM name_age')
    data = c.fetchall()
    for kol in data:
        print(kol)
read_db()
