### PYTHON TO JYSON ######

#import json as js
#
#appDict = {
#    'name': 'Roblox',
#    'playstore': True,
#    "appstore" : True,
#    "company" : "Roblox",
#    "Price" : None
#}
#app_json = js.dumps(appDict)
#print(app_json) 


##### WRITING JSON TO A FILE ####
#import json
#
#personDict = {
#  'bill': 'tech',
#  'federer': 'tennis',
#  'ronaldo': 'football',
#  'woods': 'golf',
#  'ali': 'boxing'
#}
#
#with open('person.txt', 'w') as json_file:
#  json.dump(personDict, json_file)


#### WRITING JSON TO A FILE ####
import json
def tryal():
    personDict = {}
    schema = dict(Fname = "firstName")
    for key,value in schema.items():
        personDict[key] = input('Please enter your {}: '.format(value))
        asking = input("Do you want to add another entry yes(Y) or no(N):  ")
        if asking == "Y" or asking == "y" or asking == "Yes" or asking == "yes":
            tryal()
            with open('person.json') as f:
                data = json.load(f)
            data.update(personDict)
            with open('person.json','w') as f:
                json.dump(data, f)
        else:
            print("Goodbye.")
            with open('person.json') as f:
                data = json.load(f)
            data.update(personDict)
            with open('person.json','w') as f:
                json.dump(data, f)
tryal()