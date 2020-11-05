 
import json

#### JSON
jsondict = """{
"Stream7":[{
    "7 North":{
    "pupil1":"John",
    "classTeacher":"Mr.Kamau"
    },
    "7 South":{
    "pupil2":"Mathen",
    "classTeacher":"Mrs.Mary"
    },
    "7 East":{
    "pupil3":"James",
    "classTeacher":"Mr.Mwangi"
    },
    "7 West":{
    "pupil4":"Mary",
    "classTeacher":"Mrs.Kandas"
    },
    "7 North East":{
    "pupil5":"Peter",
    "classTeacher":"Mrs.Kamau"
    },
    "7 North West":{
    "pupil1":"Mathew",
    "classTeacher":"Mrs. Mwangi"
    }
    }]
}"""    
to_python = json.loads(jsondict)
print(to_python)
#to_json = json.dump(jsondict)