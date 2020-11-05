import json as js
x = '{"name":"Nesh", "age":11, "city":"Nairobi"}'
# Converting JSON to Python
y = js.loads(x)

print(y["name"])