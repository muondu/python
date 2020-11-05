import json

def write_stuff():
#    dictionary = {"awsome_in":"Booga Booga","awsome_youtuber" : True, "noob_in_Booga Booga" : False}

    dictionary = {}
    schema = dict(Fname = "What is your name:  ")
    for keys,value in schema.items():
        
        dictionary[keys] = input("your n {} ".format(value))
        print(dictionary)
        
        with open('add_contex.txt') as f:
            data = json.load(f)
        data.update(dictionary)        
        
        with open('add_contex.txt','w') as f:
            json.dump(data,f)
            
write_stuff()

def read_stuff():
#    file = open('add_contex.json','r')
    file = open('add_contex.txt','r')
    for textin in file:
        print(textin)
read_stuff()