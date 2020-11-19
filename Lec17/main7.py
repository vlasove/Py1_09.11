"""
Считывание из json
"""

import json 

data = None 
with open("data.json", "r") as fhand:
    data = json.load(fhand)
    

print(data, type(data), len(data))
for key, val in data.items():
    print("Key:", key, "Val:", val)