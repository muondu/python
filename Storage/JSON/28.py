import json

x = {
  "name": "Nesh",
  "age": 11,
  "married": False,
  "divorced": False,
  "children": False,
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))