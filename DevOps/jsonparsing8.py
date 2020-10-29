import json 
   
# Data to be written 
dictionary ={ 
    "name" : "sathiyajith", 
    "rollno" : 56, 
    "cgpa" : 8.6, 
    "phonenumber" : "9976770500"
} 
   
with open("D:\Data\git-deep\python-poc\DevOps\sample.json", "w") as outfile: 
    json.dump(dictionary, outfile) 

f = open('D:\Data\git-deep\python-poc\DevOps\sample.json',mode='r')
data = json.load(f)
print(json.dumps(data, indent = 4, sort_keys=True))