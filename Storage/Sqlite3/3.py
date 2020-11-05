conn = sqlite3.connect('3.db')
c = conn.cursor()

def create_table():
#    c.execute('CREATE TABLE IF NOT EXISTS name_age(name1 TEXT, name2 TEXT, age INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS games(name TEXT)')
    
create_table()

def update_db():
    while True:
        name_game = input("Enter the name of the game:  ")
#        name2 = str(input("Enter your second name: "))
#        age = int(input("Enter your age: "))
        if not name1.isalpha():
            continue
        else:
            c.execute("INSERT INTO games(name) VALUES(?)",(name_game,))
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
