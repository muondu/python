from tinydb import TinyDB
db = TinyDB('4.json')
channels = db.table('Channels')
channels.insert({"name":"Nicolodean","know_it":True})
channels.insert({"name":"Carton Network","know_it":True})
channels.insert({"name":"Boomerang","know_it":True})
channels.insert({"name":"KTN","know_it":False})
channels.insert({"name":"Citizen","know_it":True})