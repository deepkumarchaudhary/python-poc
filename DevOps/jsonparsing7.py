import json 
   
# Opening JSON file 
f = open('D:\Data\git-deep\python-poc\DevOps\emp.json',mode='r') 
   
# returns JSON object as  
# a dictionary 
data = json.load(f) 
   
# Iterating through the json 
# list 
for i in data['emp_details']:
    print(i)
    print(json.dumps(i, indent = 4, sort_keys=True))
    #print(i['emp_name']) 
    #print(i['mail']) 
    #print(i['age'])
   
# Closing file 
f.close() 