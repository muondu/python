
import json

#### JSON
jsondict = """{q`e1
"profile":{
    "name":"Frank",
    "work":"Earlycamp",
    "age":50
    }
}"""    
to_python = json.loads(jsondict)
print(to_python)