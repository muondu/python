import sqlite3
import time
import datetime
import random
conn = sqlite3.connect('7.db')
c = conn.cursor()

def create_table():
#    c.execute('CREATE TABLE IF NOT EXISTS videoGames(name TEXT, Date_made REAL, price TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datastamp TEXT, Keyword TEXT, value REAL)')
    

def input_data():
#    c.execute("INSERT INTO videoGames VALUES('Minecraft', 2001, 'FREE/PAY')")
    c.execute("INSERT INTO stuffToPlot VALUES(145125552, 2016-01-02, 'Python',8)")
#    c.execute("INSERT TO videoGames VALUES('Roblox', 2015, 'FREE')")   
    conn.commit()
    
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute('INSERT INTO stuffToPlot (unix, datastamp, keyword, value) VALUES (?, ?, ?, ?)',
             (unix, date, keyword, value))
    
    conn.commit()
    
    
    
def read_from_db():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)
    
#create_table()
#input_data()
#
#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)
read_from_db()
c.close()
conn.close()