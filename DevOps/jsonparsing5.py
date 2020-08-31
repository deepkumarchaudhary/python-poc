import json
person_dict = {"name" : "Deepak",
"Age" : 35,
"Location" : "Delhi"
}

with open('D:\Data\Python-poc\DevOps\person.txt', 'w') as json_file:
    json.dump(person_dict,json_file)

with open('D:\Data\Python-poc\DevOps\person.txt', 'r') as f:
    f.read()