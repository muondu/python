import json
a_dict = {"newKey":"newValue","Nesh":"Malli","Dub":454.55}
with open('test.json') as f:
    data = json.load(f)
data.update(a_dict)
with open('test.json','w') as f:
    json.dump(data,f)