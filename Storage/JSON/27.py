import json

x = {
  "name": "Nesh",
  "age": 11,
  "married": False,
  "divorced": False,
  "pets": None,
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)