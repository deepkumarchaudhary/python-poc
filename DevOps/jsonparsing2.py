import json

with open('D:\Data\git-deep\python-poc\DevOps\details.json') as f:
    data = json.load(f)
#person = '{"name": "Bob", "languages": ["English", "Fench"]}'
#person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print (data)
print(json.dumps(data, indent = 4, sort_keys=True)) #Formatting and Beautify JSON

# Output: ['English', 'French']
print (data['languages'])
