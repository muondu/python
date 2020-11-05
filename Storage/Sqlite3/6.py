import sqlite3
conn = sqlite3.connect('6.db')
c = conn.cursor()

#c.execute("""CREATE TABLE name_and_age(
#        first text,
#        age integer
#    
#
#    )""")
#c.execute("INSERT INTO name_and_age VALUES ('Sharon','13')")

c.execute("SELECT * FROM name_and_age WHERE first='Sharon'")

print(c.fetchall())
conn.commit()
conn.close()
