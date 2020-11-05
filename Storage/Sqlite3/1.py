import sqlite3
conn = sqlite3.connect('1.db')
c = conn.cursor()
def logic():
    c.execute('CREATE TABLE IF NOT EXISTS yahoo(name TEXT ,job TEXT)')
    c.execute('INSERT INTO yahoo(name, job) VALUES(Frank, Ealrycamp)')
    conn.commit()
logic()
c.execute('CREATE TABLE IF NOT EXISTS yahoo(name TEXT job TEXT)')
c.execute('INSERT INTO yahoo VALUES("Frank", "Ealrycamp")')
conn.commit()