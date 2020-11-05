import json as  jy

x =  {
    "name":"Nesh",
    "age" : 11,
    "city" : "Nairobi"
}
# Changing Python to JS
y = jy.dumps(x)

print(y)