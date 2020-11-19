import json 

data = {
    'id' : 10,
    "name" : "Bob",
    "info" : ["info1", "info2", "info3"],
    "sex" : True,
    "Salary" : 10000.500,
    "WAT" : None
}


with open('data.json', "w") as fhand:
    json.dump(data, fhand, indent=4)