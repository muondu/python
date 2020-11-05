import json
a = input("Enter your first name:  ")
b = input("Enter your second name:  ")
a_dict = {"name1":a,"name2":b,}
with open('test3.json') as f:
    data = json.load(f)
data.update(a_dict)
with open('test3.jso','w') as f:
    json.dump(data,f)