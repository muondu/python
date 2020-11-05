from tinydb import TinyDB

db = TinyDB('2.json')
name1 = db.table('STUDENTS')
name1.insert({"Name":"Austin","Age":13})
name1.insert({"Name":"Joy","Age":13})
name1.insert({"Name":"Josh","Age":12})
name1.insert({"Name":"James","Age":11})