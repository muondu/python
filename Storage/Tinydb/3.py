from tinydb import TinyDB 
db = TinyDB('3.json')
table1 = db.table('Cakes')
input1 = input("Enter the cake name:  ")
input2 = input("Enter if it is famous:  ")
dictionary1 = dict(input1)
dictionary2 = dict(input2)
table1.insert({"name":"Red velvet","famous":True})
table1.insert({"name":"Vannila Kolida cake","famous":False})