
from tinydb import TinyDB
db = TinyDB('1.json')
table1 = db.table('Cakes')
table1.insert({"Name":"Oreo","Taste":"Good","Like_it":True})

table2 = db.table('Lolipops')
table2.insert({"Name":"Big Daddy","Taste":"Horrible","Like_it":False})