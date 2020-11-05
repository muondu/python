
import json as js

print(js.dumps({"name": "John", "age": 30}))
print(js.dumps(["apple", "bananas"]))
print(js.dumps(("apple", "bananas")))
print(js.dumps("hello"))
print(js.dumps(42))
print(js.dumps(31.76))
print(js.dumps(True))
print(js.dumps(False))
print(js.dumps(None))